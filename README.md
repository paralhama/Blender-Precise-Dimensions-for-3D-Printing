# Blender Precise Dimensions for 3D Printing
Blender add-on that displays object dimensions in mm with clean decimal formatting no trailing zeros. Built for 3D printing workflows.
## What it does
The native Blender dimensions panel can lose precision or display values without decimals. 
This add-on adds a clean panel in the sidebar that shows X, Y, Z dimensions in mm exactly as they are no rounding, no trailing zeros.
| Exact size of the object | Size displayed by Blender | Size displayed by this add-on |
|-------|---------------|-------------|
| 87.2499 mm | 87.2 mm | 87.2499 mm |
| 102 mm | 102 mm | 102 mm |
| 37.4994 mm | 37.5 mm | 37.4994 mm |

## Why this matters for slicing
When you export a model from Blender and open it in a slicer (Cura, PrusaSlicer, Bambu Studio, etc.), the slicer reads the raw geometry it does not apply Blender's unit display rounding. This means a discrepancy between what Blender's native panel shows and the actual size the slicer will use.
Precise Dimensions shows the exact value the slicer will receive no rounding, no surprises.

## Requirements
- Blender 3.0 or higher
- Unit system set to **Metric**, length set to **Millimeters**, scale **0.001**
## Installation
1. Download `Blender Precise Dimensions for 3D Printing.py`
2. Open Blender and go to **Edit → Preferences → Add-ons**
3. Click **Install** and select the downloaded file
4. Enable the checkbox next to **Precise Dimensions**
## Usage
Open the sidebar in the 3D Viewport with `N`, then go to the **Item** tab.
The **Precise Dimensions** panel will show the X, Y, Z values of the selected object in mm.
> :warning: **Important:** This add-on is designed for `Unit Scale = 0.001`. Using scale `1.0` will display incorrect values.
<img width="1902" height="819" alt="github" src="https://github.com/user-attachments/assets/82968871-54e6-40ef-ad2a-876e7337176d" />
