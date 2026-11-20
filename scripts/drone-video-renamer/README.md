# Drone video renamer

[`rename_drone_videos.py`](rename_drone_videos.py) renames the videos on a drone or FPV camera SD card so each file says which aircraft shot it and when:

```text
<DroneName>-<YYYY-MM-DD>-<suffix>.<ext>
```

| Before | After |
| --- | --- |
| `DJI_20240131_142530_0001.MP4` | `Hyper-2024-01-31-142530.mp4` |
| `clip-2025-06-01.mov` | `Hyper-2025-06-01-a264a29c.mov` |
| `VID00002.AVI` | `Hyper-2026-03-05-b1f47b26.avi` (with `--date 2026-03-05`) |

It only uses the Python 3 standard library. You don't need ffmpeg, exiftool, or any packages.

## Usage

The script only shows a preview unless you pass `--apply`.

```bash
# Preview what would change
python3 scripts/drone-video-renamer/rename_drone_videos.py Hyper /Volumes/SD_CARD/DCIM/100MEDIA

# Rename for real
python3 scripts/drone-video-renamer/rename_drone_videos.py Hyper /Volumes/SD_CARD/DCIM/100MEDIA --apply

# Put back the original names
python3 scripts/drone-video-renamer/rename_drone_videos.py --undo /Volumes/SD_CARD/DCIM/100MEDIA/rename_log_20261119_210056.csv
```

| Argument | What it does |
| --- | --- |
| `drone` | Drone name. Characters other than letters, numbers, and `_` become `_` (`"Mini 4 Pro"` becomes `Mini_4_Pro`). |
| `paths` | Files or folders to rename. Defaults to the current folder. |
| `--apply` | Rename the files. Without it, the script only prints a preview. |
| `--date YYYY-MM-DD` | Use this date for every file. Use it when the drone's clock is wrong. |
| `--uuid` | Always use a random UUID suffix instead of a timestamp. |
| `--keep-original` | Add the original name to the end, like `Hyper-2026-03-05-b1f47b26-VID00002.avi`. |
| `-r`, `--recursive` | Include subfolders. |
| `--undo LOG` | Undo an earlier run using its `rename_log_*.csv`. |

## How the name is built

**Date**, using the first source that has one:

1. `--date`
2. A date in the original file name, such as `20240131` or `2024-01-31`
3. The recording date stored in the file: the `mvhd` atom for MP4 and MOV, and the `IDIT` chunk for AVI
4. The file's modified time
5. Today's date

**Suffix**, using the first source that has one:

1. The `HHMMSS` time in the original file name
2. The recording time stored in the file
3. A random 8-character UUID

Dates before 2010 or in the future count as missing. Many drones reset their clock to something like 2018-01-01 or 2101-01-02 when they lose power. The modified time can still be wrong in a way that looks real, so check the preview and pass `--date` if needed.

## Safety

- It never overwrites a file. If two videos would get the same name, it adds `_2`, `_3`, and so on.
- It skips files that already start with `<DroneName>-YYYY-MM-DD-`, so running it again is safe.
- It ignores the macOS `._` AppleDouble files that show up on SD cards.
- Every `--apply` run writes `rename_log_<timestamp>.csv` (old path, new path) next to the videos. `--undo` reads that file.

Supported extensions: `.mp4`, `.mov`, `.avi`, `.mkv`, `.m4v`, `.mts`, `.ts`, `.3gp`, `.insv`, `.lrv`.
