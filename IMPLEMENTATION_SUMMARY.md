# Zone Styling Implementation Summary

## Overview
Created a comprehensive, abstract zone styling system for Tecplot 360 that automatically configures zone visualization based on ZoneType auxiliary data. The system processes all zones in a dataset and applies appropriate layer and visibility settings.

## Architecture

### Core Components

#### 1. `zone_style_config.py`
Defines the configuration class hierarchy:

- **`StyleConfig`** (abstract base class)
  - Abstract method: `apply_zone_style(zone)`
  - Ensures all layer configs follow the same interface

- **Layer Configuration Classes** (inherit from `StyleConfig`)
  - `ScatterConfig`: Controls scatter plot layers (symbol, color, size)
  - `MeshConfig`: Controls mesh lines (visibility, color, thickness)
  - `ContourConfig`: Controls contour layers (visibility)
  - `ShadeConfig`: Controls surface shading (visibility, color)
  - `VectorConfig`: Controls vector fields (visibility)
  - `EdgeConfig`: Controls zone edges (visibility)

- **`ZoneStyleConfig`** (main orchestrator class)
  - Composes all layer config objects
  - Manages zone visibility via fieldmap active status
  - Single `apply_zone_style()` method orchestrates all layer styling
  - Default: All layers disabled, zone disabled

#### 2. `apply_zone_styles.py`
Main script that:

1. Connects to Tecplot 360 session
2. Reads zones from active dataset
3. Extracts ZoneType aux data from each zone
4. Looks up appropriate styling config from `defaultdict`
5. Applies per-zone customizations (color, size from aux data)
6. Applies all styles to each zone

## Zone Type Configurations

| ZoneType | Layers Enabled | Zone Enabled | Special Properties |
|----------|---|---|---|
| (None/No ZoneType) | None | No | Default: all disabled |
| FullVolumeZone | None | Yes | Container zone, all styling hidden |
| Atoms | Scatter | Yes | Sphere symbol, color from AtomColor, size from log(AtomElementNumber) |
| CriticalPoints | Scatter | No | Sphere, size 1.0 |
| CriticalPoints Nuclear | Scatter | Yes | Sphere, white, size 4.0 |
| CriticalPoints Bond | Scatter | Yes | Sphere, red, size 2.5 |
| CriticalPoints Ring | Scatter | Yes | Sphere, green, size 1.0 |
| CriticalPoints Cage | Scatter | Yes | Octahedron, cyan, size 1.0 |
| AtomSphereData | Contour + Shade | Yes | Shade color from AtomColor |
| GradientPath | Mesh | Yes | Color from AtomColor, line thickness 0.2 |
| BondPath | Mesh | Yes | Black lines, thickness 0.4 |

## Key Features

### Scalable Design
- Per-layer configs allow fine-grained control
- Easy to add new zone types by adding entries to `defaultdict`
- Minimal code duplication through composition

### Auxiliary Data Integration
- Automatically extracts `AtomColor` and `AtomElementNumber` aux data
- Color mapping: string → Color enum
- Atom size formula: `ATOM_MIN_SPHERE_SIZE + log(AtomElementNumber + 1)`
- Configurable minimum sphere size via constant

### Error Handling
- Graceful handling of missing aux data
- Try-catch blocks prevent script failure on individual zone errors
- Informative error messages for debugging

### Zone Visibility Control
- Uses `plot.active_fieldmap_indices` to manage zone visibility
- Maintains existing active zones when enabling/disabling specific zones

## Usage

```bash
# Run in directory with Tecplot 360 connected
python apply_zone_styles.py
```

The script will:
1. Connect to Tecplot 360 session
2. Process all 58 zones in the example dataset
3. Apply appropriate styling to each zone
4. Print zone-by-zone processing status

## Extension Points

To add a new zone type:

```python
zone_styles["NewZoneType"] = ZoneStyleConfig(
    zone_enabled=True,  # or False
    scatter_config=ScatterConfig(...),
    mesh_config=MeshConfig(...),
    # ... other layer configs ...
)
```

To modify layer-specific attributes, update the corresponding config class's `__init__` method and `apply_zone_style` method.

## Constants

- `ATOM_MIN_SPHERE_SIZE = 4.0`: Minimum sphere size for atom zones
- Adjustable via the constant at top of `apply_zone_styles.py`

## Files Created

1. `/src/zone_style_config.py` (309 lines)
   - All configuration classes
   - Layer-specific styling logic

2. `/src/apply_zone_styles.py` (260 lines)
   - Main entry point
   - Zone type configurations
   - Aux data extraction
   - Styling orchestration

3. `/TODO.md`
   - Implementation plan and progress tracking
