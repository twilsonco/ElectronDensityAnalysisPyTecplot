# Electron Density Analysis - PyTecplot Zone Styling

A comprehensive Python system for automating zone visualization styling in Tecplot 360 EX. This project provides an abstract, scalable zone styling framework that automatically configures zone visualization based on ZoneType auxiliary data.

## Project Overview

This project implements a sophisticated zone styling system for Tecplot 360 EX that:

- **Automatically configures visualization** of zones based on their ZoneType metadata
- **Supports multiple visualization layers**: scatter plots, mesh lines, contours, surface shading, vectors, and zone edges
- **Integrates auxiliary data** from zones (colors, element numbers, etc.)
- **Provides a scalable architecture** for adding new zone types and styling configurations
- **Handles batch processing** of large datasets with multiple zones

### Key Use Cases

- Visualizing electron density data with critical points and gradient paths
- Automating zone layer configuration for complex multi-zone datasets
- Batch processing of Tecplot sessions for reproducible analysis
- Configurable styling based on zone metadata

## Architecture

### Core Components

- **`zone_style_config.py`**: Defines the configuration class hierarchy for zone styling
  - `StyleConfig`: Abstract base class for all layer configurations
  - Layer-specific configs: `ScatterConfig`, `MeshConfig`, `ContourConfig`, `ShadeConfig`, `VectorConfig`, `EdgeConfig`
  - `ZoneStyleConfig`: Main orchestrator that applies all layer styling

- **`apply_zone_styles.py`**: Main script that processes all zones in the active Tecplot dataset
- **`apply_zone_styles_batch.py`**: Batch processing script for multiple Tecplot sessions
- **`explore_data_set.py`**: Utility for exploring dataset structure and metadata
- **`hello_world.py`**: Simple example demonstrating basic API usage

## Requirements

- **Python**: 3.13+
- **Tecplot 360 EX**: Current or recent version with PyTecplot enabled
  - PyTecplot must be installed as part of Tecplot 360 EX
  - Tecplot must be accessible on the system PATH
- **Dependencies**:
  - pytecplot >= 1.7.1
  - numpy >= 2.3.2
  - protobuf >= 6.32.0
  - pyzmq >= 27.0.2

## Setup Instructions

### Prerequisites

Ensure you have:
- **Python 3.13+** installed on your system
- **`uv` package manager** installed ([install uv](https://docs.astral.sh/uv/getting-started/installation/))
- **Tecplot 360 EX** installed with PyTecplot enabled
- **Environment setup** so that Python can find the Tecplot installation (see [Tecplot Configuration](#tecplot-configuration) below)

### Setup on New Machine

#### 1. Clone or Download the Repository

```bash
git clone <repository-url>
cd ElectronDensityAnalysisPyTecplot
```

#### 2. Create Virtual Environment with `uv`

```bash
uv venv
```

This creates a `.venv` directory with Python 3.13 (or your system default Python 3.13+).

#### 3. Activate Virtual Environment

On macOS/Linux:
```bash
source .venv/bin/activate
```

On Windows:
```bash
.venv\Scripts\activate
```

#### 4. Install Dependencies

```bash
uv pip install pytecplot numpy protobuf pyzmq
```

Or, if a `pyproject.toml` or `requirements.txt` file exists:
```bash
uv pip install -r requirements.txt
```

Or using `uv sync` (if project has `uv.lock`):
```bash
uv sync
```

#### 5. Verify Installation

```bash
python -c "import tecplot; print(f'PyTecplot version: {tecplot.__version__}')"
```

If you encounter an import error, see the [Tecplot Configuration](#tecplot-configuration) section below.

### Tecplot Configuration

#### macOS/Linux Setup

For Tecplot 360 EX to be accessible to Python, you may need to configure environment variables depending on your Tecplot installation location.

**Option 1: Automatic Discovery**

If Tecplot 360 EX is installed in the standard location, PyTecplot should be automatically discovered. Verify with:

```bash
python -c "import tecplot; print(tecplot.__file__)"
```

**Option 2: Manual Configuration**

If automatic discovery fails, you need to set the `TECPLOTSDK` environment variable to point to your Tecplot 360 EX installation.

1. **Find your Tecplot installation directory:**
   ```bash
   # Common macOS locations:
   /Applications/Tecplot360EX/bin
   /opt/tecplot/360ex/bin
   
   # Common Linux locations:
   /opt/tecplot360ex/bin
   /home/username/.tecplot/360ex/bin
   ```

2. **Set environment variables:**

   Add to your `~/.zshrc`, `~/.bashrc`, or equivalent shell configuration:
   
   ```bash
   # For macOS
   export TECPLOTSDK="/Applications/Tecplot360EX"
   export DYLD_LIBRARY_PATH="$TECPLOTSDK/lib:$DYLD_LIBRARY_PATH"
   export PYTHONPATH="$TECPLOTSDK/lib/python:$PYTHONPATH"
   
   # For Linux
   export TECPLOTSDK="/opt/tecplot360ex"
   export LD_LIBRARY_PATH="$TECPLOTSDK/lib:$LD_LIBRARY_PATH"
   export PYTHONPATH="$TECPLOTSDK/lib/python:$PYTHONPATH"
   ```

3. **Apply the changes:**
   ```bash
   source ~/.zshrc  # or ~/.bashrc for bash
   ```

4. **Verify the import works:**
   ```bash
   python -c "import tecplot; print(f'PyTecplot version: {tecplot.__version__}')"
   ```

#### Windows Setup

On Windows, PyTecplot should be automatically discoverable if Tecplot 360 EX is installed in the default location.

If not, set the environment variable:

1. Open **Environment Variables** (search in Windows Start menu)
2. Add a new system variable:
   - **Variable name:** `TECPLOTSDK`
   - **Variable value:** `C:\Program Files\Tecplot\360EX` (or your installation path)
3. Add to `PATH` if needed:
   - `C:\Program Files\Tecplot\360EX\bin`
4. Restart any open terminals or IDEs
5. Verify:
   ```cmd
   python -c "import tecplot; print(f'PyTecplot version: {tecplot.__version__}')"
   ```

## Usage

### Basic Workflow

1. **Start Tecplot 360 EX** with your data file loaded
2. **Ensure your Python environment is activated:**
   ```bash
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate     # Windows
   ```
3. **Run the styling script**:
   ```bash
   python src/apply_zone_styles.py
   ```
4. The script will automatically connect to the running Tecplot session and apply zone styling based on ZoneType metadata

### Batch Processing

For processing multiple files:

```bash
python src/apply_zone_styles_batch.py
```

### Exploring Data

To inspect dataset structure and zone properties:

```bash
python src/explore_data_set.py
```

### Example Usage

```python
from zone_style_config import ZoneStyleConfig, ScatterConfig
import tecplot

# Connect to running Tecplot 360 EX instance
tecplot.session.connect()

# Get the active dataset
dataset = tecplot.active_frame().dataset

# Create a custom configuration
config = ZoneStyleConfig(zone_enabled=True, scatter_config=ScatterConfig(...))

# Apply to a zone
for zone in dataset.zones():
    config.apply_zone_style(zone)
```

## Zone Type Configurations

The system comes with predefined configurations for:

| ZoneType | Enabled | Layers | Description |
|----------|---------|--------|-------------|
| FullVolumeZone | Yes | None | Container zone (all styling hidden) |
| Atoms | Yes | Scatter | Atomic positions with color/size from metadata |
| CriticalPoints | Varies | Scatter | Critical points in electron density |
| AtomSphereData | Yes | Contour + Shade | Electron density around atoms |
| GradientPath | Yes | Mesh | Gradient paths between points |
| BondPath | Yes | Mesh | Bond paths connecting atoms |

See `IMPLEMENTATION_SUMMARY.md` for detailed zone type specifications.

## Project Structure

```
.
├── README.md                      # This file
├── IMPLEMENTATION_SUMMARY.md      # Detailed architecture documentation
├── notes.md                       # Development notes and references
├── pytecplot_docs/                # Local PyTecplot documentation
├── src/
│   ├── zone_style_config.py       # Configuration classes
│   ├── apply_zone_styles.py       # Main styling script
│   ├── apply_zone_styles_batch.py # Batch processing
│   ├── explore_data_set.py        # Dataset exploration utility
│   └── hello_world.py             # Simple example
└── .venv/                         # Virtual environment (created by uv)
```

## Documentation

- **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)**: Comprehensive architecture and design documentation
- **[notes.md](notes.md)**: Development notes and reference links
- **[PyTecplot Documentation](pytecplot_docs/)**: Local copy of official PyTecplot API docs

### External References

- [Tecplot 360 User Manual](https://tecplot.azureedge.net/products/360/2013r1m1/adkum.pdf)
- [PyTecplot Official Docs](https://tecplot.azureedge.net/products/pytecplot/docs/index.html)
- [Tecplot 360 Macro Scripting Guide](https://tecplot.azureedge.net/products/360/current/360-scripting-guide.pdf)

## Development

### Virtual Environment Management

Update dependencies:
```bash
uv pip install --upgrade pytecplot numpy protobuf pyzmq
```

Export current environment:
```bash
uv pip freeze > requirements.txt
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'tecplot'"

This indicates that PyTecplot cannot be found. Solutions:

1. **Verify Tecplot 360 EX is installed:**
   ```bash
   # macOS
   ls -la /Applications/Tecplot360EX/
   
   # Linux
   ls -la /opt/tecplot360ex/
   
   # Windows - check Program Files\Tecplot\360EX
   ```

2. **Configure environment variables** as described in [Tecplot Configuration](#tecplot-configuration) section above

3. **Ensure the virtual environment is activated:**
   ```bash
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate     # Windows
   ```

4. **Test the import directly:**
   ```bash
   python -c "import sys; print(sys.path)"
   python -c "import tecplot; print(tecplot.__file__)"
   ```

### PyTecplot Connection Issues

- **"Cannot connect to Tecplot"**: Ensure Tecplot 360 EX is running and accessible on localhost
- **"Connection refused"**: Make sure Tecplot 360 EX has PyTecplot/scripting enabled (typically enabled by default)
- **Platform mismatch**: Ensure your Python architecture (32-bit vs 64-bit) matches your Tecplot installation
- **Network issues**: PyTecplot communicates via ZMQ. Check that firewall is not blocking local connections

### Missing Dependencies

```bash
# Reinstall all dependencies
uv pip install --upgrade pytecplot numpy protobuf pyzmq
```

### Virtual Environment Problems

```bash
# Remove and recreate virtual environment
rm -rf .venv
uv venv
source .venv/bin/activate
uv pip install pytecplot numpy protobuf pyzmq
```

### Library Loading Errors (Linux)

If you see errors like "cannot open shared object file," update library paths:

```bash
export LD_LIBRARY_PATH="/opt/tecplot360ex/lib:$LD_LIBRARY_PATH"
python src/apply_zone_styles.py
```

Or add this to your `~/.bashrc` or `~/.zshrc` for persistent configuration.

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

## Authors

[Add author information here]

---

**Last Updated**: 2026-08-12  
**Python Version**: 3.13+  
**Package Manager**: uv 0.7.9+
