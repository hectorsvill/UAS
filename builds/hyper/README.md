# Hyper

3-inch 3S build on a Kabab FPV Toothpick 3 (TP3) frame, named for its Pyrodrone Hyperlite 1303.5 5022KV motors. Planning, collecting spare parts.

| Spec | Detail |
| --- | --- |
| Status | Planning, collecting spare parts. Betaflight 2026.6.2 on MATEKF411; Bluejay 0.21.0 flashed; setup in progress |
| Frame | Kabab FPV Toothpick 3 (TP3). 3-inch props. The listing says it accepts a 1"×1" typical whoop mounting platform; exact hole spacing is not stated there. About 11–12 g built with hardware; 1.5 mm body plates, 3 mm arms. On hand: TBD. The SoloGood Fi-135 is a spare and is not used on this build |
| Motors | Pyrodrone Hyperlite 1303.5 5022KV ×4 (2–4S, discontinued). On hand, confirm |
| FC/ESC | DarwinFPV F411 AIO, a spare from a DarwinFPV BabyApe Pro V4. STM32F411, 25.5×25.5 mm mount, fit-checked on the Fi-135 (that frame is now spare). ESC 15A continuous / 17A burst, EFM8BB21, Bluejay 0.21.0 on layout S-H-50 (was BLHeli_S 16.7). 1–3S only. 5V/2A BEC. Onboard analog OSD (AT7456E). On hand. The HDZero Gamma 45A AIO is still reserved for a later 3.5-inch 6S build, not this one |
| VTX | PandaRC VT5804 analog VTX, already attached to the Darwin board, with an analog camera on this build. VTX table loaded; UART2 set to TBS SmartAudio (switch to IRC Tramp if channel changes don't follow). The DJI O4 Air Unit is a spare / for other builds and is not used on Hyper |
| RX | ExpressLRS 2.4 GHz EP2 RX nano (SX1280) on UART1 via CRSF. RadioMaster Pocket is the ELRS radio |
| Battery | 3S, capacity TBD |
| Props | 3-inch 2-blade, 3018/3020 class. 5022KV is high for aggressive triblades on 3S |
| AUW | TBD. I will weigh it before the first flight. On a recreational flight, 250 g (0.55 lb) or less means I don't register or broadcast Remote ID. More than 250 g means I register, mark, and broadcast, or fly at a FRIA. |
| Operating mode | Recreational by default. I only fly this aircraft under Part 107 for a project. |
| Remote ID | I have not chosen the hardware yet. If I fly it recreationally at 250 g (0.55 lb) or less, I don't register it and don't broadcast Remote ID. If it weighs more than 250 g, I register it, mark the registration number on the outside, and broadcast with built-in Standard Remote ID or a module, unless I fly at a FRIA, stay inside the boundary, and keep it in sight. Under Part 107 I register and broadcast at any weight. |
| Betaflight config | See Betaflight & ESC setup below. Link `configs/betaflight/hyper/` here once a dump exists |
| Brain note | The full parts list with prices lives in my private notes |

## Firmware

I flashed Betaflight 4.5.5 with build options CRSF, OSD Digital, and DSHOT, plus the defaults, with full chip erase on. The board was previously on Betaflight 4.2.5 with the MATEKF411 target. OSD Digital was for the earlier DJI O4 plan. This build now uses the board's onboard analog OSD (AT7456E), so I will use analog OSD in Betaflight.

The DARWINF411 target did not detect the gyro. `status` showed `SPI:0`, `Gyros detected: locked`, and the arming flag `NOGYRO`. Reflashing with the MATEKF411 target fixed it; the gyro now works. Use MATEKF411 for this board.

Planned wiring:

- UART1 = ExpressLRS 2.4 GHz EP2 RX nano (SX1280) via CRSF
- UART2 is no longer needed for MSP DisplayPort (the O4 is not on this build)
- VTX control (SmartAudio / IRC Tramp) wiring and UART: TBD
- OSD: onboard analog OSD (AT7456E); use analog OSD in Betaflight

The old 4.2.5 config had gyro alignment CW180. I will verify orientation in the Setup tab.

The 2026-11-18 reflash and current ports, VTX, and ESC setup are under Betaflight & ESC setup below.

## Betaflight & ESC setup

Recorded 2026-11-18.

### Firmware

- Betaflight 2026.6.2, target MATEKF411 (community target) on the Darwin F411 AIO
- Build options: CRSF radio, Analog OSD, DSHOT, VTX, Pin IO
- Recommended to drop GPS, Altitude Hold, Position Hold, LED Strip, and Acro Trainer to save flash
- Full chip erase before flash

### Board alignment

- USB faces up (board flipped)
- Set roll 180°
- To verify: Setup tab 3D model should match nose-down and roll-right

### Ports

| Port | Setting |
| --- | --- |
| USB VCP | MSP on |
| UART1 | Serial RX (EP2 ELRS, CRSF) |
| UART2 | Peripheral VTX (TBS SmartAudio) at 115200. Switch to IRC Tramp if channel changes don't follow |

### VTX

- PandaRC VT5804 AIR
- VTX table loaded from [PandaRC's VTX configuration file](https://pandarc.net/pages/vtx-configuration-file)
- 40 channels on A/B/E/F/R; power 0/25/50/100/200/400 mW
- Power from VBAT (6–26 V input, not 5V)
- Suggested:

```
set vtx_low_power_disarm = ON
save
```

### CPU load

OSD showed CPU overload on this F411. Fix:

```
set pid_process_denom = 2
save
```

That is a 4 kHz PID loop. Use `3` or `4` if the warning stays. Target CPU load under ~70% via `status`.

### ESC

- Was BLHeli_S 16.7, layout S-H-50
- Flashed Bluejay 0.21.0 at 48 kHz via [ESC Configurator](https://esc-configurator.com/)
- Motor directions: M1 Reversed, M2 Normal, M3 Reversed, M4 Normal

| Setting | Value |
| --- | --- |
| Startup power min / max | 1010 / 1020 |
| Timing | 22.5° (MediumHigh) |
| Demag | Low |
| RPM power protection | 9x |
| Beep | 40 |
| Beacon | 80 |
| Beacon delay | 10 min |
| Power rating | 2S+ |
| Temp protection | Disabled |
| Brake on stop | Off |
| Max brake | 255 |

### Bidirectional DShot

DSHOT300, bidirectional DShot on. `dshot_telemetry_info` at idle:

- 0.00% invalid packets on all 4 motors
- ESC temp telemetry 20–31 °C

### Still to do

- Verify motor order and direction on the Motors tab (props off)
- Set motor poles:

```
set motor_poles = 12
save
```

- Confirm the RPM filter is on
- OSD, battery, modes, and failsafe
- Save a `diff all` baseline

## Next steps

Remaining setup is listed under Betaflight & ESC setup.

## Photos

I store photos in the `images/` folder next to this README and link them with relative paths; I keep each image under ~1 MB.

<!-- ![Hyper top view](images/hyper-top.jpg) -->
<!-- ![Hyper side view](images/hyper-side.jpg) -->
<!-- ![Hyper FC/AIO wiring close-up](images/hyper-fc-wiring.jpg) -->
<!-- ![Hyper VTX + antenna](images/hyper-vtx-antenna.jpg) -->
<!-- ![Hyper receiver mounting](images/hyper-receiver.jpg) -->
<!-- ![Hyper complete build with battery](images/hyper-complete.jpg) -->

## Build log

- 2026-11-16: Build started. Parts list opened.
- 2026-11-16: I chose the spare Darwin F411 AIO and flashed Betaflight 4.5.5. DARWINF411 did not detect the gyro; MATEKF411 does. I will use MATEKF411 for this board.
- 2026-11-17: I switched the frame to the Kabab FPV Toothpick 3 (TP3). The receiver is an ExpressLRS 2.4 GHz EP2 RX nano (SX1280) on UART1 via CRSF. Video is the PandaRC VT5804 already attached to the Darwin board, with an analog camera. The Fi-135 and the O4 are spares and are not used on Hyper.
- 2026-11-18: I reflashed Betaflight 2026.6.2 (MATEKF411, Analog OSD), loaded the VT5804 VTX table, and set UART2 to TBS SmartAudio. I flashed Bluejay 0.21.0 at 48 kHz and verified bidirectional DShot.

## Links

- [Hyperlite 1303.5 5022KV (archived listing)](https://web.archive.org/web/20230201022401/https://pyrodrone.com/products/hyperlite-1303-5-fpv-drone-motor-5022kv)
- [Kabab FPV Toothpick 3 (TP3) frame](https://fpvcycle.com/products/kabab-toothpick-3-tp3-frame)
