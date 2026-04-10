# Blender Print Dimensions

Blender add-on that displays object dimensions in mm with clean decimal formatting — no trailing zeros. Built for 3D printing workflows.

## What it does

The native Blender dimensions panel can lose precision or display values without decimals. This add-on adds a clean panel in the sidebar that shows X, Y, Z dimensions in mm exactly as they are — no rounding, no trailing zeros.

| Value | Native Blender | This add-on |
|-------|---------------|-------------|
| 113.2 mm | 113 mm | 113.2 mm |
| 25.50 mm | 25.5 mm | 25.5 mm |
| 10.125 mm | 10.12 mm | 10.125 mm |

## Requirements

- Blender 3.0 or higher
- Unit system set to **Metric**, length set to **Millimeters**, scale **1**

## Installation

1. Download `dimensions_panel.py`
2. Open Blender and go to **Edit → Preferences → Add-ons**
3. Click **Install** and select the downloaded file
4. Enable the checkbox next to **Print Dimensions**

## Usage

Open the sidebar in the 3D Viewport with `N`, then go to the **Item** tab. The **Dimensions** panel will show the X, Y, Z values of the selected object in mm.

## License

MIT
