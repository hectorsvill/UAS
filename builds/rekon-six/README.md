# Rekon Six

Status: On the bench

5-inch 6S build on an HGLRC Rekon 5 Lite frame, with iFlight XING 2005 1900KV motors, a SpeedyBee F405 AIO 40A, TBS Crossfire, and a planned DJI O4 Lite.

| Spec | Detail |
| --- | --- |
| Status | On the bench. Collecting parts and planning the build |
| Frame | HGLRC Rekon 5 Lite frame kit, 206 mm wheelbase, 5-inch ([Amazon listing](https://www.amazon.com/dp/B0FX3TVQ7N), [official page](https://www.hglrc.com/products/hglrc-rekon-5-llite-frame)). Official specs: flight controller mounts 25.5 × 25.5 mm M2, VTX mounts 20 × 20 / 25.5 × 25.5 mm M2, motor mounts 12 × 12 mm M2, camera width 19 / 20 mm, mounting height 26 mm, 5 mm carbon, frame weight 52 g. The kit includes a canopy, an integrated power board, a battery anti-slip pad, and two battery ties |
| Motors | iFlight XING 2005 1900KV unibell ×4 ([Pyrodrone listing](https://pyrodrone.com/products/iflight-xing-2005-4-6s-fpv-unibell-motor-1900kv), [official page](https://shop.iflight.com/xing-2005-4-6s-fpv-motor-unibell-pro1381)). 4–6S. Official specs: 21 g with wires, 12 × 12 mm φ2 mm mounting holes, 1.5 mm shaft (4 mm protruding), 12N14P, peak current 19.37 A. Motor mounts match the frame (12 × 12 mm). Props need a 1.5 mm shaft; iFlight lists Nazgul 5030 or any other 1.5 mm shaft prop |
| FC/ESC | SpeedyBee F405 AIO 40A ([official page](https://www.speedybee.com/speedybee-f405-aio-40a-bluejay-25-5x25-5-3-6s-flight-controller/)). STM32F405, ICM-42688P gyro, 3–6S, 40A continuous / 45A burst (10 s), Bluejay JH-40 48 kHz, current sensor scale 254 / offset 0, firmware target SPEEDYBEE F405AIO. Mounting is 25.5 × 25.5 mm with 2 mm holes, which matches the Rekon 5 Lite stack holes. The same official page lists the board size two ways (33.0 × 33.0 × 8 mm in the specs table, 36.5 × 36.5 × 7.0 mm in the fit note), so I'll confirm the board clears the stack when I install it. Four full UARTs (UART3, UART4, UART5, UART6, plus SBUS on R2). 5V BEC, 2A total; no onboard 9V BEC (an external module is included). The 6-pin DJI Sky Port is listed for O3 / RunCam Link / Caddx Vista; I'll confirm O4 Lite wiring before I plug it in. The official page lists this board as discontinued; I already have it |
| VTX | DJI O4 Lite, planned. Antenna TBD |
| RX | TBS Crossfire Nano RX ([official page](https://www.team-blacksheep.com/products/prod:crossfire_nano_rx)) via CRSF, controlled from a TBS Tango 2. Official specs: 11 × 18 × 11 mm, 0.5 g, 3.3–8.4 V input, CRSF / SBUS / PPM / PWM. UART assignment TBD |
| Battery | 6S, capacity TBD. The frame kit includes a battery anti-slip pad and two battery ties |
| Props | 5-inch, TBD. Need a 1.5 mm shaft (the motor also uses a 6 × 6 prop pattern) |
| AUW | TBD. I will weigh it before the first flight. On a recreational flight, 250 g (0.55 lb) or less means I don't register or broadcast Remote ID. More than 250 g means I register, mark, and broadcast, or fly at a FRIA. |
| Operating mode | Recreational by default. I only fly this aircraft under Part 107 for a project. |
| Remote ID | I have not chosen the hardware yet, and I have not confirmed that the O4 Lite is on an [FAA-accepted Remote ID Declaration of Compliance](https://uasdoc.faa.gov/). If I fly it recreationally at 250 g (0.55 lb) or less, I don't register it and don't broadcast Remote ID. If it weighs more than 250 g, I register it, mark the registration number on the outside, and broadcast with built-in Standard Remote ID or a module, unless I fly at a FRIA, stay inside the boundary, and keep it in sight. Under Part 107 I register and broadcast at any weight. |
| Betaflight config | See Betaflight & ESC setup and Full CLI config below. Link `configs/betaflight/rekon-six/` here once a dump exists |
| Brain note | The full parts list with prices lives in my private notes |

## Firmware

Not flashed yet. The official target name is SPEEDYBEE F405AIO. I'll record the Betaflight version and build options when I flash it.

## Betaflight & ESC setup

Not started. Planned ports: one UART for the Crossfire Nano RX (CRSF), and another for the O4 Lite (MSP DisplayPort) once that is installed. The F405 AIO has four full UARTs, so there is room for GPS later if I add it.

### Still to do

- Flash Betaflight (target SPEEDYBEE F405AIO)
- Confirm O4 Lite wiring on the 6-pin port
- Wire and bind the Crossfire Nano RX
- Choose 5-inch props (1.5 mm shaft), 6S packs, an XT60 pigtail, and a low-ESR capacitor
- Confirm Remote ID hardware
- Weigh the aircraft before the first flight

## Next steps

Remaining parts and setup are listed under Still to do.

## Photos

I'll add photos in the `images/` folder once the build is together. I keep each image under ~1 MB and link them with relative paths.

## Parts list (copy/paste)

Caption I can paste to Instagram or X:

```text
Rekon Six
Frame: HGLRC Rekon 5 Lite (206 mm)
FC/ESC: SpeedyBee F405 AIO 40A
Motors: iFlight XING 2005 1900KV
RX: TBS Crossfire Nano RX
Radio: TBS Tango 2
VTX: DJI O4 Lite (planned)
Firmware: TBD
Battery: 6S
Props: 5-inch, TBD
#fpv #fpvdrone #betaflight #crossfire
```

## Build log

- 2026-11-21: Build started. I chose the name Rekon Six. Parts on hand or chosen: Rekon 5 Lite frame, XING 2005 1900KV motors, SpeedyBee F405 AIO 40A, and a TBS Crossfire Nano RX. I'm planning a DJI O4 Lite for video.

## Links

- [HGLRC Rekon 5 Lite frame (official)](https://www.hglrc.com/products/hglrc-rekon-5-llite-frame)
- [HGLRC Rekon 5 Lite frame kit (Amazon)](https://www.amazon.com/dp/B0FX3TVQ7N)
- [iFlight XING 2005 4–6S unibell (official)](https://shop.iflight.com/xing-2005-4-6s-fpv-motor-unibell-pro1381)
- [iFlight XING 2005 1900KV (Pyrodrone)](https://pyrodrone.com/products/iflight-xing-2005-4-6s-fpv-unibell-motor-1900kv)
- [SpeedyBee F405 AIO 40A (official)](https://www.speedybee.com/speedybee-f405-aio-40a-bluejay-25-5x25-5-3-6s-flight-controller/)
- [TBS Crossfire Nano RX (official)](https://www.team-blacksheep.com/products/prod:crossfire_nano_rx)
- [FAA Remote ID](https://www.faa.gov/uas/getting_started/remote_id)
- [FAA Remote ID Declaration of Compliance list](https://uasdoc.faa.gov/)

## PIDs & rates

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

Reproduce this config from a fresh Betaflight flash of the same target (after defaults). `defaults` is not needed after a full chip erase. `acc_calibration` is board-specific, so recalibrate the accelerometer instead of pasting it.

```
# paste CLI commands here
save
```
