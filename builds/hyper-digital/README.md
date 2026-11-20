# Hyper Digital

<!-- Top photos: images/hyper-digital-front.jpg and images/hyper-digital-right.jpg, side by side at width 45%, once I have them. -->

Photos TBD.

Status: On the bench

Digital version of [Hyper Analog](../hyper/README.md). Uses the same FC, motors, and ExpressLRS EP2 nano as Hyper Analog, on a SoloGood 3-inch frame with a DJI O4 Lite (O4 Air Unit) for digital video, because analog video quality was poor.

| Spec | Detail |
| --- | --- |
| Status | On the bench. Planned 2026-11-19. Mount, wire, and maiden still to do |
| Frame | SoloGood 3-inch carbon frame for DJI O4 ([Amazon listing](https://www.amazon.com/dp/B0F1F5YSMS): 3 Inch Micro Carbon Fiber FPV Racing Quadcopter Frame For DJI O4 Air Unit). Wheelbase 135 mm, about 33 g, 14 mm camera bay, FC mounts 25.5×25.5 / 26.5×26.5 / 20×20 mm. 3K carbon; 3 mm bottom plate, 2 mm top plate, 1.5 mm side plates, 24 mm standoffs |
| Motors | Pyrodrone Hyperlite 1303.5 5022KV ×4 (2–4S, discontinued). Same as [Hyper Analog](../hyper/README.md) |
| FC/ESC | DarwinFPV F411 AIO, the same FC as [Hyper Analog](../hyper/README.md). STM32F411, 25.5×25.5 mm mount. ESC 15A continuous / 17A burst, EFM8BB21, Bluejay 0.21.0 on layout S-H-50 (was BLHeli_S 16.7). 1–3S only. 5V/2A BEC. See [Hyper Analog](../hyper/README.md) for the ESC setup |
| VTX | DJI O4 Lite (O4 Air Unit). MSP DisplayPort on UART2. Power from VBAT |
| RX | ExpressLRS 2.4 GHz EP2 RX nano (SX1280) on UART1 via CRSF. Same as [Hyper Analog](../hyper/README.md) |
| Battery | 3S, capacity TBD. Do not run the O4 Lite on 4S |
| Props | 3-inch 2-blade, 3018/3020 class. 5022KV is high for aggressive triblades on 3S |
| AUW | TBD. I will weigh it before the first flight. On a recreational flight, 250 g (0.55 lb) or less means I don't register or broadcast Remote ID. More than 250 g means I register, mark, and broadcast, or fly at a FRIA. |
| Operating mode | Recreational by default. I only fly this aircraft under Part 107 for a project. |
| Remote ID | I have not chosen the hardware yet. If I fly it recreationally at 250 g (0.55 lb) or less, I don't register it and don't broadcast Remote ID. If it weighs more than 250 g, I register it, mark the registration number on the outside, and broadcast with built-in Standard Remote ID or a module, unless I fly at a FRIA, stay inside the boundary, and keep it in sight. Under Part 107 I register and broadcast at any weight. |
| Betaflight config | See Betaflight & ESC setup and Full CLI config below. Link `configs/betaflight/hyper-digital/` here once a dump exists |
| Brain note | The full parts list with prices lives in my private notes |

## Firmware

Same flash as [Hyper Analog](../hyper/README.md) until I confirm otherwise: Betaflight 2026.6.2, target MATEKF411 (community target) on the Darwin F411 AIO. The DARWINF411 target did not detect the gyro; use MATEKF411. Build options on Hyper Analog were CRSF, Analog OSD, DSHOT, VTX, and Pin IO. I may need a rebuild with digital OSD for MSP DisplayPort; TBD after I wire the O4.

## Wiring

The O4 Lite 3-in-1 cable has no solder pads at the air-unit end, so I cut the FC end and solder it to the pads the VT5804 used on [Hyper Analog](../hyper/README.md). Pinout is from the [DJI O4 Air Unit Series user manual](https://dl.djicdn.com/downloads/DJI_O4_Air_Unit_Series/UM/DJI_O4_Air_Unit_Series_User_Manual_v1.0_en.pdf). TX goes to RX, so the O4's white wire lands on TX2. I'll check the pad labels on the board before I solder.

| O4 wire | Signal | Darwin F411 pad |
| --- | --- | --- |
| Red | VCC (3.7–13.2 V) | VBAT (the old VTX power pad) |
| Black | Power GND | GND |
| White | O4 RX | TX2 (where SmartAudio was) |
| Grey | O4 TX | RX2 |
| Brown | Signal GND | Not connected |
| Yellow | S.Bus | Not connected (I'm on ELRS) |

The O4 Lite input is 3.7–13.2 V, so a full 3S pack at 12.6 V on VBAT is within spec. Never run it on 4S. I'll add a low-ESR 220–470 µF, 25 V cap on the battery leads to soak up voltage spikes.

## Betaflight & ESC setup

Planned 2026-11-19. Not wired yet.

### Firmware

- Betaflight 2026.6.2, target MATEKF411 (community target) on the Darwin F411 AIO
- Build options: same as Hyper Analog for now (CRSF, Analog OSD, DSHOT, VTX, Pin IO); digital OSD rebuild is TBD
- Full chip erase before flash, if I reflash

### Board alignment and motor remap

If the FC mounting orientation differs from Hyper Analog, I have to recheck board alignment and the motor resource remap. Hyper Analog uses `align_board_roll = 180` and MOTOR 1 B06, 2 B07, 3 B04, 4 B05 (USB up, board flipped, props-in). I will confirm in the Setup tab after I mount it.

### Ports

| Port | Setting |
| --- | --- |
| USB VCP | MSP on |
| UART1 | Serial RX (EP2 ELRS, CRSF) at 115200 |
| UART2 | MSP DisplayPort at 115200 (replaces TBS SmartAudio) |

### Modes

Same as Hyper Analog until I change them:

- Arm on AUX1 (1700–2100)
- Flip over after crash (turtle) on AUX2 (1700–2100)

### VTX

- Model: DJI O4 Lite (O4 Air Unit)
- Control: MSP DisplayPort on UART2
- Power source: VBAT
- Remove the analog VTX table
- In the goggles, set the O4 OSD to Canvas mode (HD)

### Betaflight changes vs Hyper Analog

After wiring, with props off:

```
serial UART2 1 115200 57600 0 115200
set osd_displayport_device = MSP
set vcd_video_system = HD
save
```

Then delete the VTX table on the Video Transmitter tab, and set the goggles OSD to Canvas mode.

### CPU load

TBD after the swap. Digital OSD should be a bit lighter than the analog chip. If the OSD shows CPU overload, check `status` once it's past boot.

### Rates

I'll start from Hyper Analog's Actual rates (center 200, max 670 deg/s roll/pitch, yaw srate 60, expo 54) and tighten them if I want it snappier. See PIDs & rates below.

### ESC

Same Bluejay setup as [Hyper Analog](../hyper/README.md): Bluejay 0.21.0 at 48 kHz, layout S-H-50, M1 Reversed, M2 Normal, M3 Reversed, M4 Normal, `motor_poles = 12`. Recheck directions after I mount the motors.

### Bidirectional DShot

Same as Hyper Analog (DSHOT300, bidirectional DShot on). I'll confirm with `dshot_telemetry_info` after the swap.

### Still to do

- Mount and wire
- Confirm board alignment and motor remap
- Verify OSD in the goggles, props off
- Maiden
- Rates and PID tune
- Full CLI config once it's flying

## Next steps

Remaining setup is listed under Betaflight & ESC setup.

## Photos

I store photos in the `images/` folder next to this README and link them with relative paths; I keep each image under ~1 MB.

Photos TBD. I'll add back and left shots here, side by side at width 45%, once I take them.

<!--
<p align="center">
  <img src="images/hyper-digital-back.jpg" alt="Hyper Digital back" width="45%">
  <img src="images/hyper-digital-left.jpg" alt="Hyper Digital left side" width="45%">
</p>
-->

## Parts list (copy/paste)

Caption I can paste to Instagram or X:

```text
Hyper Digital 3S
Frame: SoloGood 3-inch carbon (DJI O4)
FC/ESC: DarwinFPV F411 AIO 15A (Bluejay 0.21.0)
Motors: Pyrodrone Hyperlite 1303.5 5022KV
RX: ELRS EP2 nano
VTX: DJI O4 Lite
Firmware: Betaflight 2026.6.2
Battery: 3S
Props: 3-inch 2-blade, 3018/3020 class
#fpv #fpvdrone #dji #o4lite #betaflight #expresslrs
```

## Build log

- 2026-11-19: Planned. Digital version of [Hyper Analog](../hyper/README.md) on the SoloGood 3-inch frame with a DJI O4 Lite. Uses the same FC, motors, and EP2 receiver as Hyper Analog. Mount, wire, and maiden still to do.

## Links

- [SoloGood 3-inch carbon frame for DJI O4](https://www.amazon.com/dp/B0F1F5YSMS)
- [DJI O4 Air Unit Series user manual](https://dl.djicdn.com/downloads/DJI_O4_Air_Unit_Series/UM/DJI_O4_Air_Unit_Series_User_Manual_v1.0_en.pdf)
- [Hyper Analog](../hyper/README.md)
- [Hyperlite 1303.5 5022KV (archived listing)](https://web.archive.org/web/20230201022401/https://pyrodrone.com/products/hyperlite-1303-5-fpv-drone-motor-5022kv)

## PIDs & rates

PIDs are Betaflight 2026.6.2 defaults (untuned) unless noted. I'll start from Hyper Analog's rates and tune after the maiden.

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

Reproduce this config from a fresh Betaflight 2026.6.2 MATEKF411 flash (after defaults) once the build is flying. `defaults` is not needed after a full chip erase. `acc_calibration` is board-specific, so recalibrate the accelerometer instead of pasting it. ESC direction is set in ESC Configurator, not CLI. Board alignment and the motor remap depend on how I mount the FC, so I will not paste Hyper Analog's remap until I confirm orientation.

```
# paste CLI commands here after the swap
serial UART2 1 115200 57600 0 115200
set osd_displayport_device = MSP
set vcd_video_system = HD
save
```
