# Hyper

3-inch 3S build on a SoloGood Fi-135, named for its Pyrodrone Hyperlite 1303.5 5022KV motors. Planning, collecting spare parts.

| Spec | Detail |
| --- | --- |
| Status | Planning, collecting spare parts. Flight controller flashed; gyro working on the MATEKF411 target |
| Frame | SoloGood Fi-135 O4 kit (3-inch; 24 mm columns, favors an AIO). On hand: TBD |
| Motors | Pyrodrone Hyperlite 1303.5 5022KV ×4 (2–4S, discontinued). On hand, confirm |
| FC/ESC | DarwinFPV F411 AIO, a spare from a DarwinFPV BabyApe Pro V4. STM32F411, 25.5×25.5 mm mount, fit-checked on the Fi-135. ESC 15A continuous / 17A burst, EFM8BB21, BLHeli_S/Bluejay layout S-H-50. 1–3S only. 5V/2A BEC, so I have to power the O4 from 3S VBAT (O4 input is 3.7–13.2 V). On hand. The HDZero Gamma 45A AIO is still reserved for a later 3.5-inch 6S build, not this one |
| VTX | DJI O4 Air Unit (standard), powered from 3S VBAT. On hand: TBD. The PandaRC VT5804 analog VTX is a spare and is not used on this build |
| RX | UART1 via CRSF, which works for both Crossfire and ExpressLRS. RadioMaster Pocket is the ELRS radio. Receiver hardware: TBD |
| Battery | 3S, capacity TBD |
| Props | 3-inch 2-blade, 3018/3020 class. 5022KV is high for aggressive triblades on 3S |
| AUW | TBD. I will weigh it before the first flight. On a recreational flight, 250 g (0.55 lb) or less means I don't register or broadcast Remote ID. More than 250 g means I register, mark, and broadcast, or fly at a FRIA. |
| Operating mode | Recreational by default. I only fly this aircraft under Part 107 for a project. |
| Remote ID | I have not chosen the hardware yet. If I fly it recreationally at 250 g (0.55 lb) or less, I don't register it and don't broadcast Remote ID. If it weighs more than 250 g, I register it, mark the registration number on the outside, and broadcast with built-in Standard Remote ID or a module, unless I fly at a FRIA, stay inside the boundary, and keep it in sight. Under Part 107 I register and broadcast at any weight. |
| Betaflight config | See Firmware below. Link `configs/betaflight/hyper/` here once a dump exists |
| Brain note | The full parts list with prices lives in my private notes |

## Firmware

I flashed Betaflight 4.5.5 with build options CRSF, OSD Digital, and DSHOT, plus the defaults, with full chip erase on. The board was previously on Betaflight 4.2.5 with the MATEKF411 target.

The DARWINF411 target did not detect the gyro. `status` showed `SPI:0`, `Gyros detected: locked`, and the arming flag `NOGYRO`. Reflashing with the MATEKF411 target fixed it; the gyro now works. Use MATEKF411 for this board.

Planned wiring:

- UART1 = receiver via CRSF (Crossfire or ExpressLRS)
- UART2 = DJI O4 as MSP DisplayPort

The old 4.2.5 config had gyro alignment CW180. I will verify orientation in the Setup tab.

## Next steps

- Ports, receiver, OSD, battery, modes, and failsafe setup
- Flash Bluejay S-H-50 and enable bidirectional DShot + RPM filter (motor poles, usually 12; count the magnets)
- Check motor direction
- Save a `diff all` baseline

## Build log

- 2026-11-16: Build started. Parts list opened.
- 2026-11-16: I chose the spare Darwin F411 AIO and flashed Betaflight 4.5.5. DARWINF411 did not detect the gyro; MATEKF411 does. I will use MATEKF411 for this board.

## Links

- [Hyperlite 1303.5 5022KV (archived listing)](https://web.archive.org/web/20230201022401/https://pyrodrone.com/products/hyperlite-1303-5-fpv-drone-motor-5022kv)
- [DJI O4 Air Unit Series user manual v1.0](https://dl.djicdn.com/downloads/DJI_O4_Air_Unit_Series/UM/DJI_O4_Air_Unit_Series_User_Manual_v1.0_en.pdf)
