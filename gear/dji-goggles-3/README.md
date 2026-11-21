# DJI Goggles 3

Notes for my DJI Goggles 3, used with the DJI O4 Air Unit (Lite) on [Hyper Digital](../../builds/hyper-digital/README.md).

Official manuals:

- [DJI O4 Air Unit Series User Manual v1.0](https://dl.djicdn.com/downloads/DJI_O4_Air_Unit_Series/UM/DJI_O4_Air_Unit_Series_User_Manual_v1.0_en.pdf)
- [DJI Goggles 3 User Manual v1.0](https://dl.djicdn.com/downloads/DJI_Goggles_3/20240528/DJI_Goggles_3_User_Manual_EN.pdf) (from the [Goggles 3 downloads page](https://www.dji.com/goggles-3/downloads))

## Activation and firmware

Activate the goggles and the air unit before first use, and update both to the latest firmware before linking.

If the goggles are not activated, only linking works, the menu cannot be operated, and the link stays on the public channel. If the air unit is not activated, transmission power is limited (≤20 mW) and the connected goggles menu cannot be operated. ([O4 manual, §3.1](https://dl.djicdn.com/downloads/DJI_O4_Air_Unit_Series/UM/DJI_O4_Air_Unit_Series_User_Manual_v1.0_en.pdf))

**Goggles.** Connect the goggles' USB-C port to a phone with the USB-C OTG cable and a data cable, open [DJI Fly](https://www.dji.com/goggles-3/downloads), and follow the on-screen instructions to activate and update. The phone needs an internet connection. ([Goggles 3 manual, Activation](https://dl.djicdn.com/downloads/DJI_Goggles_3/20240528/DJI_Goggles_3_User_Manual_EN.pdf))

Firmware can also be updated in [DJI Assistant 2 (Consumer Drones Series)](https://www.dji.com/downloads/softwares/dji-assistant-2-consumer-drones-series):

1. Power on the goggles and connect them to the computer with a USB-C cable.
2. If you are using the USB-C fast charging cable, open the goggles menu, go to **Settings > About**, and enter **OTG Wired Connection** mode.
3. Launch Assistant 2, log in with a DJI account, select the device, and click **Firmware Update**.
4. Select the firmware version and wait. The goggles restart when the update finishes. Keep the computer online, leave the cable plugged in, and make sure the goggles have enough power.

([Goggles 3 manual, Updating Firmware](https://dl.djicdn.com/downloads/DJI_Goggles_3/20240528/DJI_Goggles_3_User_Manual_EN.pdf))

**O4 Air Unit (Lite).** Download Assistant 2 (Consumer Drones Series) from the [O4 Air Unit downloads page](https://www.dji.com/o4-air-unit/downloads). Take the props off, power on the air unit, and connect it to the computer with a USB-C cable. Launch Assistant 2, log in, and activate the unit from the on-screen prompts. Then select the product, click the firmware update button, pick the version, and wait. Restart the air unit when the update finishes. ([O4 manual, §3.1–3.2](https://dl.djicdn.com/downloads/DJI_O4_Air_Unit_Series/UM/DJI_O4_Air_Unit_Series_User_Manual_v1.0_en.pdf))

## Pairing with the O4 Lite

These steps follow the O4 manual's Goggles 3 linking example ([§3.4](https://dl.djicdn.com/downloads/DJI_O4_Air_Unit_Series/UM/DJI_O4_Air_Unit_Series_User_Manual_v1.0_en.pdf)) and the Goggles 3 manual for product selection and the Power Button/Link Button. Update firmware first. I use ELRS on Hyper Digital, so I skip linking a DJI remote controller.

1. Power on the air unit and the goggles.
2. Open the goggles menu, select **Status**, and use the upper right corner to select the product (the Goggles 3 manual labels this **Switch**). Choose the O4 Air Unit.
3. Confirm the air unit's linking status indicator is red. Press the air unit **link button** once. The indicator blinks red.
4. Press and hold the goggles **Power Button/Link Button** until the goggles beep continuously and the battery level LEDs blink in sequence.
5. When linking succeeds, the air unit indicator turns solid green, the goggles stop beeping, and live view appears.

Air unit linking status indicator, from those official linking steps:

| Indicator | Meaning |
| --- | --- |
| Red | Ready to link |
| Blinking red | Linking |
| Solid green | Linked; live view should appear |

Keep the devices close while linking. The Goggles 3 manual says within 0.5 m, with enough battery.

Official walkthrough: [DJI O4 Air Unit Series linking video](https://www.dji.com/o4-air-unit/video).

## Canvas Mode (Betaflight OSD)

DJI calls this Canvas Mode. It lets the flight controller draw OSD elements on the goggles screen. The official setup is in Betaflight. The Goggles 3 and O4 manuals (v1.0) do not list a Custom OSD or Canvas toggle in the Goggles 3 menu.

On [Hyper Digital](../../builds/hyper-digital/README.md), UART2 is already set to **VTX (MSP + Displayport)**. Official basic steps ([O4 manual, §4.6](https://dl.djicdn.com/downloads/DJI_O4_Air_Unit_Series/UM/DJI_O4_Air_Unit_Series_User_Manual_v1.0_en.pdf)), using UART2 in place of DJI's UART4 example:

1. Connect the air unit UART RX to a flight controller UART TX (UART2 on Hyper Digital).
2. In Betaflight Configurator **Ports**, set that UART's **Peripherals** to **MSP+Displayport** (Configurator 4.4.0 or later), then Save and Reboot. That replaces the older CLI:

```
set osd_displayport_device = MSP
set displayport_msp_serial = 1
save
```

`displayport_msp_serial` is the UART number minus 1, so UART2 is 1. DJI's example uses UART4 and `3`.

3. In the **OSD** tab, set the video format to HD and turn on the elements you want. The Hyper Digital build has the layout I use.

## Stream the goggles view to a Mac (USB-C, no capture card)

Two community tools can show the Goggles 3 live view on a Mac over a single USB-C data cable. They are unofficial and reverse-engineered, so a DJI firmware update may break them. They carry video only, with no audio. The OSD is already in the picture.

### GogglesView (gogglecast)

[GogglesView](https://github.com/Kristian-Buriasco/gogglecast) is a native macOS app for Apple Silicon, macOS 14 or later. It can show live view at up to 60 fps, record the raw stream with no re-encode to `~/Movies/GogglesView`, open a chrome-less window for OBS Window Capture, and stream out over RTMP or SRT. Virtual camera is experimental; if it stays black in OBS, use Window Capture instead.

Setup, from the [GogglesView README](https://github.com/Kristian-Buriasco/gogglecast):

1. Unplug the goggles.
2. On the goggles, go to **Settings > About** and enable **OTG Wired Connection to Computer**.
3. Reconnect with a USB-C cable that carries data, not a charge-only cable.
4. Start live view (quad powered and linked). Then open the app.

### DJI Goggles Bridge

[DJI Goggles Bridge](https://github.com/Evols/dji-goggles-bridge) is a Mac and Windows app. Download the macOS archive from [Releases](https://github.com/Evols/dji-goggles-bridge/releases), extract it, and run:

```sh
./dji-goggles-bridge-macos
```

Setup, from the [Goggles Bridge README](https://github.com/Evols/dji-goggles-bridge):

1. Power on the goggles and connect a USB-C data cable. Close other goggles apps.
2. Turn on **Settings > About > OTG Wired Connection to Computer**. The goggles should show **OTG Wired Connection - Connected**.
3. Press the **5D button down, towards you**, to open the shortcut menu, and turn on **Share Liveview to Mobile Device via Wi-Fi**. This also enables video over USB.
4. Confirm a live camera picture in the goggles.

Choose option **2** in the app to share the stream, then:

- **OBS:** add a Media Source, uncheck Local File, set Input to `udp://127.0.0.1:5600`, and set Input Format to `mpegts`.
- **VLC:** Media > Open Network Stream, then `udp://@127.0.0.1:5600`.

## Notes

My goggles run from an external LiPo through a UBEC, so the OSD goggle battery percentage does not track pack state. Check pack voltage instead.
