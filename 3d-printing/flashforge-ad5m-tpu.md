# TPU printing on the Flashforge Adventurer 5M

Setup notes for printing drone parts (antenna mounts, camera damper pads) in TPU with Flash Studio.

## Hardware and filament

| Item | Value |
|---|---|
| Printer | Flashforge Adventurer 5M (direct-drive extruder, 280 °C max) |
| Slicer | Flash Studio |
| Nozzle | **0.4 mm stainless**. Do not use 0.25 mm for TPU, it clogs. |
| Filament | Overture TPU, 1.75 mm, black (hardness not on the label; believed 95A) |
| Label ranges | Nozzle 210–230 °C, bed 25–60 °C, speed 20–40 mm/s |

The slicer's nozzle setting (Printer section) must match the nozzle installed on the printer.

## Filament preset

Save as a **User preset**: `Overture TPU 1.75 - 0.4 nozzle` (start from Generic TPU, then edit with the pencil icon next to the filament name).

**Filament tab**

| Setting | Value |
|---|---|
| Nozzle, first layer / other layers | 225 / 225 °C (Generic TPU defaults to 255 / 240, too hot) |
| Bed (Smooth or Textured PEI row), first / other | 50 / 45 °C |
| Pressure advance | Off |

**Cooling tab**

| Setting | Value |
|---|---|
| No cooling for the first | 2 layers |
| Min fan speed threshold, fan speed | 50% |
| Max fan speed threshold, fan speed | 60% |
| Auxiliary part cooling fan | 50% |
| Keep fan always on / Slow printing for layer cooling | On |
| Don't slow down outer walls | Off |
| Force cooling for overhangs and bridges | On |
| Exhaust fan | Off |

Max volumetric speed is not exposed in this version. At 25–30 mm/s with 0.16 mm layers the flow stays near 2 mm³/s, so it isn't needed.

## Process preset

Save as a **User preset**, for example `0.16mm TPU Antenna Mount @AD5M 0.4` (start from a 0.4 mm Standard preset).

| Tab | Setting | Value |
|---|---|---|
| Quality | Layer height / first layer | 0.16 / 0.20 mm |
| Quality | Seam | Aligned (or Back); Precise wall on |
| Strength | Walls | 3 |
| Strength | Top / bottom layers | 5 / 4 |
| Strength | Infill | 25% gyroid (100% for the thin damper pads) |
| Support | Support | Off; tree supports only if the preview shows sagging |
| Multimaterial | Everything | Defaults, no prime tower |
| Others | Skirt | 1 loop (add a 3–5 mm brim only if corners lift) |
| Speed | Walls / infill / first layer | about 25 / 30 / 15–20 mm/s |
| Retraction | Distance | Off or 0.5–1 mm, slow |

These presets suit flexible drone parts. For rigid prints (PLA, PETG, carbon fiber), start from the stock preset instead.

## Print routine

1. Check the nozzle size installed matches the slicer (0.4 mm).
2. Dry the filament if the spool has been open for a while (wet TPU strings and prints rough).
3. Orient flat on the bed and slice. Check the Preview for gaps and overhangs.
4. Print slowly and watch the first layers.
5. When finished, unload or retract the filament carefully. TPU can jam in the extruder after a print.

## Troubleshooting

| Problem | Try |
|---|---|
| Stringing or rough surface | Dry the filament; lower the nozzle to 215–220 °C |
| Under-extrusion or clicking | Slow down; check for a partial clog; if it persists, a 0.6 mm nozzle is the fallback |
| Corners lifting | Add a 3–5 mm brim; raise the bed to 50–55 °C |
| Sagging under overhangs | Raise the fan to 70%; enable tree supports for that area |
| Part too thick for a tight fit | Scale only the Z axis in Flash Studio (flat parts keep their hole sizes) |

## Parts printed with this setup

| Part | File | Notes |
|---|---|---|
| Antenna mount (O4 Pro, Fi-135 style) | [o4pro-antenna-mount.3mf](../builds/hyper-digital/o4pro-antenna-mount.3mf) | Rear screw tubes and rear ring removed; antenna tube and 4 mm standoff holes unchanged. Print flat, base down. |
| Camera damper pad v2 (print 2) | `o4lite-camera-damper-pad-v2.stl` | Body 1.2 mm; 1.6 mm collars go into the plate holes. Camera 13.8 mm wide, plates 16.4 mm apart. Print collars up. |
