# Build README template

How to use: copy this file to `builds/<name>/README.md` and create `builds/<name>/images/`. Keep images under ~1 MB. Do not put serials or coordinates in this repo.

---

<!-- Title: the build name, first person throughout. -->
# <Build name>

<!-- Top photos: side by side, width 45%. Files: images/<build>-front.jpg and images/<build>-right.jpg. -->
<p align="center">
  <img src="images/<build>-front.jpg" alt="<Build name> front" width="45%">
  <img src="images/<build>-right.jpg" alt="<Build name> right side" width="45%">
</p>

<!-- Status line: use exactly one of: On the bench (in progress), In the hangar (currently flying), Retired. -->
Status: <On the bench | In the hangar | Retired>

<One-line description. TBD>

<!-- Specs/parts table: what is on this aircraft. Use TBD for unknowns. No serials or coordinates. -->
| Spec | Detail |
| --- | --- |
| Status | <On the bench \| In the hangar \| Retired>. TBD |
| Frame | TBD |
| Motors | TBD |
| FC/ESC | TBD |
| VTX | TBD |
| RX | TBD |
| Battery | TBD |
| Props | TBD |
| AUW | TBD. I will weigh it before the first flight. On a recreational flight, 250 g (0.55 lb) or less means I don't register or broadcast Remote ID. More than 250 g means I register, mark, and broadcast, or fly at a FRIA. |
| Operating mode | Recreational by default. I only fly this aircraft under Part 107 for a project. |
| Remote ID | TBD. If I fly it recreationally at 250 g (0.55 lb) or less, I don't register it and don't broadcast Remote ID. If it weighs more than 250 g, I register it, mark the registration number on the outside, and broadcast with built-in Standard Remote ID or a module, unless I fly at a FRIA, stay inside the boundary, and keep it in sight. Under Part 107 I register and broadcast at any weight. |
| Betaflight config | See Betaflight & ESC setup and Full CLI config below. Link `configs/betaflight/<name>/` here once a dump exists |
| Brain note | The full parts list with prices lives in my private notes |

## Firmware

<!-- Target, version, and anything I had to change to get the gyro or OSD working. -->

I flashed Betaflight <version>, target <TARGET>, with full chip erase. Build options: TBD.

## Betaflight & ESC setup

<!-- Firmware target, build options, and ESC work. Subsections follow this order. -->

Recorded <YYYY-MM-DD>.

### Firmware

- Betaflight <version>, target <TARGET>
- Build options: TBD
- Full chip erase before flash

### Board alignment and motor remap

- Board orientation: TBD
- Motor resources: TBD
- Props-in or props-out: TBD

### Ports

<!-- Ports: UART map, protocol, and baud. -->

| Port | Setting |
| --- | --- |
| USB VCP | MSP on |
| UART1 | TBD |
| UART2 | TBD |

### Modes

<!-- Modes: arm and other modes, with AUX channel and range. -->

- Arm on AUX1 (TBD)
- Other modes: TBD

### VTX

<!-- VTX: model, band, channel, power, control protocol, and power source. -->

- Model: TBD
- Band / channel / power: TBD
- Control: TBD
- Power source: TBD

### CPU load

TBD. If the OSD shows CPU overload, lower `pid_process_denom` and check `status`.

### Rates

TBD. See PIDs & rates below.

### ESC

- Firmware and layout: TBD
- Motor directions: TBD
- `motor_poles = TBD`

### Bidirectional DShot

TBD. After enabling, check with `dshot_telemetry_info`.

### Still to do

- TBD

## Next steps

Remaining setup is listed under Betaflight & ESC setup.

## Photos

<!-- Extra photos, usually back and left, side by side at width 45%. Keep files under ~1 MB in images/. -->

I store photos in the `images/` folder next to this README and link them with relative paths; I keep each image under ~1 MB.

<p align="center">
  <img src="images/<build>-back.jpg" alt="<Build name> back" width="45%">
  <img src="images/<build>-left.jpg" alt="<Build name> left side" width="45%">
</p>

## Parts list (copy/paste)

<!-- Plain-text caption for Instagram or X. One line per part. Only list parts already on this build; don't invent. -->

Caption I can paste to Instagram or X:

```text
<Build name>
Frame: TBD
FC/ESC: TBD
Motors: TBD
RX: TBD
VTX: TBD
Firmware: TBD
Battery: TBD
Props: TBD
#fpv #fpvdrone #betaflight
```

## Build log

<!-- Dated bullets, YYYY-MM-DD, first person. -->

- YYYY-MM-DD: Build started.

## Links

- TBD

## PIDs & rates

<!-- Dump commands below. `get` does a substring match. After tuning, paste `diff profile` and `diff rates` into the current-diff block. -->

PIDs are Betaflight defaults (untuned) unless noted. Rates: TBD.

Dump current values. Betaflight CLI `get` does a substring match, so these work:

```
profile 0
get p_
get i_
get d_
get f_
get d_max
rateprofile 0
get rc_rate
get srate
get expo
get rates_type
```

`diff profile` and `diff rates` show only changed values.

Current PID/rates diff:

```
# PIDs: defaults (paste diff profile here after tuning)
# paste diff rates here
```

## Full CLI config

<!-- Keep this section at the bottom. Commands to reproduce this config from a fresh flash. Omit acc_calibration (recalibrate on the board) and any serials. ESC direction is set in ESC Configurator, not CLI. -->

Reproduce this config from a fresh Betaflight flash of the same target (after defaults). `defaults` is not needed after a full chip erase. `acc_calibration` is board-specific, so recalibrate the accelerometer instead of pasting it.

```
# paste CLI commands here
save
```
