#!/usr/bin/env python3
"""
rename_drone_videos.py - Rename drone video files to:  <DroneName>-<YYYY-MM-DD>-<suffix>.<ext>

  suffix = HHMMSS timestamp found in the original file name (e.g. DJI_20240131_142530.MP4)
           otherwise the recording time stored inside the file (MP4/MOV 'mvhd', AVI 'IDIT')
           otherwise a short random UUID (8 hex chars)

  date   = --date if given, else the date from the file name, else the date stored
           inside the file, else the file's modified time (if it looks sane), else today.

Previews by default. Add --apply to actually rename. Every applied run writes an
undo log (rename_log_<time>.csv) so you can restore with --undo <logfile>.

Examples:
  python3 rename_drone_videos.py "Mini 4 Pro" /Volumes/SD_CARD/DCIM/100MEDIA            # preview
  python3 rename_drone_videos.py "Mini 4 Pro" /Volumes/SD_CARD/DCIM/100MEDIA --apply    # rename
  python3 rename_drone_videos.py Falcon . --date 2026-11-19 --apply                       # force date
  python3 rename_drone_videos.py Falcon . --uuid --apply                                  # always UUID suffix
  python3 rename_drone_videos.py --undo rename_log_20261119_204500.csv
"""

import argparse
import csv
import os
import re
import struct
import sys
import uuid
from datetime import datetime, date, timedelta, timezone
from pathlib import Path

VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".m4v", ".mts", ".ts", ".3gp", ".insv", ".lrv"}
MIN_YEAR = 2010  # anything earlier (or in the future) is treated as an unset drone clock

# YYYY MM DD [sep] HH MM SS  -> 20240131_142530, 2024-01-31 14-25-30, 20240131142530, ...
DATETIME_RE = re.compile(
    r"(?<!\d)(20\d{2})[-_.]?(\d{2})[-_.]?(\d{2})[ _T.-]?(\d{2})[-_.:]?(\d{2})[-_.:]?(\d{2})(?!\d)"
)
DATE_RE = re.compile(r"(?<!\d)(20\d{2})[-_.]?(\d{2})[-_.]?(\d{2})(?!\d)")


# ---------------------------------------------------------------- helpers
def sanitize(name: str) -> str:
    """Make a string safe for file names on macOS/Windows/Linux and SD cards."""
    name = re.sub(r"[^A-Za-z0-9_]+", "_", name.strip())
    return re.sub(r"_+", "_", name).strip("_")


def plausible(dt: datetime) -> bool:
    now = datetime.now() + timedelta(days=2)
    return datetime(MIN_YEAR, 1, 1) <= dt <= now


def datetime_from_name(stem: str):
    """Return (datetime or None, has_time: bool) parsed from the file name."""
    for m in DATETIME_RE.finditer(stem):
        try:
            dt = datetime(*map(int, m.groups()))
            if plausible(dt):
                return dt, True
        except ValueError:
            pass
    for m in DATE_RE.finditer(stem):
        try:
            dt = datetime(*map(int, m.groups()))
            if plausible(dt):
                return dt, False
        except ValueError:
            pass
    return None, False


def datetime_from_mp4(path: Path):
    """Read creation time from the 'mvhd' atom of MP4/MOV files (no ffprobe needed)."""
    try:
        size = path.stat().st_size
        with path.open("rb") as f:
            chunks = [f.read(4 * 1024 * 1024)]
            if size > 8 * 1024 * 1024:  # moov atom is often at the end
                f.seek(-4 * 1024 * 1024, os.SEEK_END)
                chunks.append(f.read())
        for data in chunks:
            i = data.find(b"mvhd")
            if i < 0 or i + 16 > len(data):
                continue
            version = data[i + 4]
            if version == 1:
                secs = struct.unpack(">Q", data[i + 8:i + 16])[0]
            else:
                secs = struct.unpack(">I", data[i + 8:i + 12])[0]
            if secs == 0:
                continue
            dt = datetime(1904, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=secs)
            dt = dt.astimezone().replace(tzinfo=None)  # most drones store UTC
            if plausible(dt):
                return dt
    except (OSError, struct.error, OverflowError):
        pass
    return None


def datetime_from_avi(path: Path):
    """Read the RIFF 'IDIT' (digitization date) chunk some cameras put in AVI files."""
    try:
        with path.open("rb") as f:
            data = f.read(256 * 1024)
        i = data.find(b"IDIT")
        if i < 0:
            return None
        n = struct.unpack("<I", data[i + 4:i + 8])[0]
        text = data[i + 8:i + 8 + n].decode("ascii", "ignore").strip("\x00 \r\n")
        for fmt in ("%a %b %d %H:%M:%S %Y", "%Y:%m:%d %H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S"):
            try:
                dt = datetime.strptime(text, fmt)
                return dt if plausible(dt) else None
            except ValueError:
                continue
    except (OSError, struct.error):
        pass
    return None


def datetime_from_metadata(path: Path):
    ext = path.suffix.lower()
    if ext in {".mp4", ".mov", ".m4v", ".3gp", ".insv", ".lrv"}:
        return datetime_from_mp4(path)
    if ext == ".avi":
        return datetime_from_avi(path)
    return None


def datetime_from_mtime(path: Path):
    dt = datetime.fromtimestamp(path.stat().st_mtime)
    return dt if plausible(dt) else None




def build_name(path: Path, drone: str, forced_date, force_uuid: bool, keep_original: bool):
    """Return (new_file_name, explanation)."""
    stem, ext = path.stem, path.suffix.lower()

    name_dt, name_has_time = datetime_from_name(stem)
    meta_dt = datetime_from_metadata(path)

    # ---- date
    if forced_date:
        d, d_src = forced_date, "--date"
    elif name_dt:
        d, d_src = name_dt.date(), "file name"
    elif meta_dt:
        d, d_src = meta_dt.date(), "video metadata"
    else:
        mt = datetime_from_mtime(path)
        if mt:
            d, d_src = mt.date(), "file modified time"
        else:
            d, d_src = date.today(), "today (no reliable date found)"

    # ---- suffix
    if force_uuid:
        suffix, s_src = uuid.uuid4().hex[:8], "uuid"
    elif name_dt and name_has_time:
        suffix, s_src = name_dt.strftime("%H%M%S"), "time from file name"
    elif meta_dt:
        suffix, s_src = meta_dt.strftime("%H%M%S"), "time from metadata"
    else:
        suffix, s_src = uuid.uuid4().hex[:8], "uuid"

    parts = [drone, d.isoformat(), suffix]
    if keep_original:
        parts.append(sanitize(stem))
    return "-".join(parts) + ext, f"date: {d_src}; suffix: {s_src}"


def unique_target(target: Path, taken: set) -> Path:
    """Avoid overwriting: add _2, _3, ... if the name already exists or is planned."""
    candidate, n = target, 2
    while candidate.exists() or str(candidate).lower() in taken:
        candidate = target.with_name(f"{target.stem}_{n}{target.suffix}")
        n += 1
    return candidate


def collect_files(paths, recursive: bool):
    files = []
    for p in map(Path, paths):
        if p.is_dir():
            it = p.rglob("*") if recursive else p.iterdir()
            files.extend(f for f in it if f.is_file())
        elif p.is_file():
            files.append(p)
        else:
            print(f"warning: not found: {p}", file=sys.stderr)
    return sorted(
        f for f in files
        if f.suffix.lower() in VIDEO_EXTS and not f.name.startswith("._")  # skip macOS AppleDouble junk
    )


def undo(log_file: Path):
    with log_file.open(newline="") as fh:
        rows = list(csv.DictReader(fh))
    for row in reversed(rows):
        src, dst = Path(row["new"]), Path(row["old"])
        if src.exists() and not dst.exists():
            src.rename(dst)
            print(f"restored  {src.name} -> {dst.name}")
        else:
            print(f"skipped   {src.name} (missing, or original name already in use)")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description="Rename drone videos to DroneName-YYYY-MM-DD-<time|uuid>.ext")
    ap.add_argument("drone", nargs="?", help='drone name, e.g. "Mini 4 Pro" -> Mini_4_Pro')
    ap.add_argument("paths", nargs="*", default=["."], help="files or folders (default: current folder)")
    ap.add_argument("--apply", action="store_true", help="actually rename (default is preview only)")
    ap.add_argument("--date", help="force a date (YYYY-MM-DD), useful when the drone clock is wrong")
    ap.add_argument("--uuid", action="store_true", help="always use a random UUID suffix")
    ap.add_argument("--keep-original", action="store_true", help="append the original name, e.g. ...-VID00002")
    ap.add_argument("-r", "--recursive", action="store_true", help="include sub-folders")
    ap.add_argument("--undo", metavar="LOG", help="undo a previous run using its rename_log CSV")
    args = ap.parse_args()

    if args.undo:
        undo(Path(args.undo))
        return
    if not args.drone:
        ap.error("drone name is required")

    drone = sanitize(args.drone)
    if not drone:
        ap.error("drone name has no usable characters")

    forced_date = None
    if args.date:
        try:
            forced_date = datetime.strptime(args.date, "%Y-%m-%d").date()
        except ValueError:
            ap.error("--date must look like 2026-11-19")

    already = re.compile(rf"^{re.escape(drone)}-\d{{4}}-\d{{2}}-\d{{2}}-", re.IGNORECASE)
    files = collect_files(args.paths, args.recursive)
    if not files:
        print("No video files found.")
        return

    plan, taken = [], set()
    for f in files:
        if already.match(f.name):
            print(f"skip      {f.name} (already renamed)")
            continue
        new_name, why = build_name(f, drone, forced_date, args.uuid, args.keep_original)
        target = unique_target(f.with_name(new_name), taken)
        taken.add(str(target).lower())
        plan.append((f, target, why))

    width = max((len(f.name) for f, _, _ in plan), default=0)
    for f, t, why in plan:
        print(f"{f.name:<{width}}  ->  {t.name}    [{why}]")

    if not plan:
        return
    if not args.apply:
        print(f"\nPreview only - {len(plan)} file(s). Re-run with --apply to rename.")
        return

    log_dir = plan[0][0].parent
    log_path = log_dir / f"rename_log_{datetime.now():%Y%m%d_%H%M%S}.csv"
    done = 0
    with log_path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["old", "new"])
        for f, t, _ in plan:
            try:
                f.rename(t)
                w.writerow([str(f.resolve().parent / f.name), str(t.resolve())])
                fh.flush()
                done += 1
            except OSError as e:
                print(f"error     {f.name}: {e}", file=sys.stderr)
    print(f"\nRenamed {done}/{len(plan)} file(s). Undo log: {log_path}")


if __name__ == "__main__":
    main()
