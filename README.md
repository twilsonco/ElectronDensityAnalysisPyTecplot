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
git clone https://github.com/twilsonco/ElectronDensityAnalysisPyTecplot.git
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

> ### IMPORTANT: Always run scripts with `python -O`
>
> **Always pass the `-O` (optimize) flag when running these scripts**, in both batch and connected mode:
>
> ```bash
> python -O src/apply_zone_styles.py
> uv run python -O src/apply_zone_styles.py
> ```
>
> **Why:** PyTecplot's `lock_attributes` decorator runs an extremely expensive
> `inspect.stack()` call on *every attribute assignment* of every Tecplot object
> (Zone, FieldMap, AuxData, Style, ...). These checks are guarded by
> `if __debug__:`, so the `-O` flag disables them entirely. Profiling this
> project's workload showed `inspect.stack()` accounting for **~57% of total
> runtime** (11 of 19 seconds). Measured on a 237-zone dataset in connected
> mode:
>
> | Command | Runtime |
> |---|---|
> | `python src/apply_zone_styles.py` | 19.2s |
> | `python -O src/apply_zone_styles.py` | 7.0s |
> | `python -O` + all code-level optimizations | **2.2s** |
>
> `run_batch.sh` already includes `-O`. For connected mode, you must pass it yourself.
>
> **What about `-OO`?** The PyTecplot documentation recommends the `-OO` flag, but
> `-O` is sufficient here. The difference: `-O` disables `assert` statements and all
> `if __debug__:` blocks (where every expensive PyTecplot run-time check lives),
> while `-OO` additionally strips docstrings — a memory saving only, with no extra
> speed benefit. Both levels skip PyTecplot's argument validation, so invalid values
> are sent to the engine instead of raising a clean Python `TecplotTypeError`; keep
> defensive `try/except` handling around styling calls accordingly.

### Running Scripts in Batch Mode (Recommended)

**Batch mode** is the recommended approach for running PyTecplot scripts. It runs significantly faster than connected mode because PyTecplot directly interfaces with the Tecplot engine libraries rather than communicating through sockets with the GUI.

#### Quick Start (macOS/Linux)

Use the provided `run_batch.sh` wrapper script to automatically handle environment setup:

```bash
# Run any script in batch mode
./run_batch.sh src/hello_world.py

# Run with arguments
./run_batch.sh src/apply_zone_styles.py --option value

# Run batch processing
./run_batch.sh src/apply_zone_styles_batch.py
```

> **Note:** The `run_batch.sh` script includes an explicit path to your Tecplot 360 EX installation. Update the path if your installation is in a different location or your version differs from `2025 R1`. The script ensures that the correct environment variables are set for Tecplot batch mode execution.

#### What run_batch.sh Does

The wrapper script:
1. Activates your Python virtual environment (`.venv`)
2. Configures Tecplot library paths using `tec360-env`
3. Runs your Python script with the correct environment

This gives you the best of both worlds:
- ✅ Your project dependencies from `.venv`
- ✅ Tecplot library paths for batch mode execution
- ✅ Significantly faster script execution than connected mode

#### Manual Setup (If Needed)

If you prefer to set up the environment manually:

```bash
# Activate virtual environment
source .venv/bin/activate

# Run with tec360-env (remember the -O flag!)
"/Applications/Tecplot 360 EX 2025 R1/bin/tec360-env" -- python -O src/script_name.py
```

> **Note:** Replace `2025 R1` with your installed version of Tecplot 360 EX.

### Batch vs. Connected Mode

| Aspect | Batch Mode | Connected Mode |
|--------|-----------|-----------------|
| **Speed** | ⚡ Fast (recommended) | 🐢 Slow (socket overhead) |
| **GUI Updates** | ❌ None (engine only) | ✅ Updates GUI in real-time |
| **Setup** | Requires `tec360-env` | Only needs venv activation |
| **Use Case** | Data processing, batch jobs | Interactive debugging |

**For this project, use batch mode** via `./run_batch.sh` for all production scripts.

#### The `apply_zone_styles_batch.py` Script: Batch Mode Processing

The `apply_zone_styles_batch.py` script provides pure batch mode processing with two modes:

```bash
# SINGLE FILE: Process one .plt file (no Tecplot instance needed)
./run_batch.sh src/apply_zone_styles_batch.py /path/to/file.plt
# → Outputs: /path/to/file.lpk

# DIRECTORY: Process all .plt files in a directory (no Tecplot instance needed)
./run_batch.sh src/apply_zone_styles_batch.py /path/to/directory
# → Processes all .plt files, outputting .lpk for each, deleting original .plt files
```

Both modes use PyTecplot batch mode, so no running Tecplot instance is required. Perfect for automated batch processing workflows.

### Script Examples

#### 1. Hello World Example

```bash
./run_batch.sh src/hello_world.py
# Outputs: hello_world.png
```

#### 2. Explore Dataset Structure

```bash
./run_batch.sh src/explore_data_set.py
# Displays: Zone types, auxiliary data, and dataset properties
```

#### 3. Apply Zone Styling (Single File - Batch Mode)

Process a single `.plt` file without needing a running Tecplot instance:

```bash
./run_batch.sh src/apply_zone_styles_batch.py /path/to/file.plt
# Outputs: /path/to/file.lpk
```

#### 4. Batch Process Multiple Files

Process all `.plt` files in a directory using batch mode (no Tecplot instance required):

```bash
./run_batch.sh src/apply_zone_styles_batch.py /path/to/directory
# For each file: loads .plt → applies styles → saves .lpk → deletes .plt
```

### Connected Mode (For Interactive Development)

If you need to interactively connect to a running Tecplot 360 EX GUI for real-time visualization:

1. **Start Tecplot 360 EX** with your data file loaded
2. **Enable PyTecplot connections:**
   - In Tecplot: `Scripting` → `PyTecplot Connections...` → Enable (default port 7600)
3. **Activate your environment and run (with `-O`!):**
   ```bash
   source .venv/bin/activate
   python -O src/apply_zone_styles.py  # Will connect to running GUI
   ```

This mode updates the visualization in real-time but is significantly slower due to socket communication overhead. The `-O` flag is especially important here — it disables PyTecplot's per-attribute `inspect.stack()` checks, which are pure Python overhead on top of the socket cost. Use batch mode (`apply_zone_styles_batch.py`) for production workflows.

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

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

For major changes, please open an issue first to discuss what you would like to change.

## Authors

**Cody T. Wilson** - Initial implementation

See [GitHub contributors](https://github.com/twilsonco/ElectronDensityAnalysisPyTecplot/graphs/contributors) for a list of contributors.

---

**Repository**: [twilsonco/ElectronDensityAnalysisPyTecplot](https://github.com/twilsonco/ElectronDensityAnalysisPyTecplot)  
**Last Updated**: 2026-08-12  
**Python Version**: 3.13+  
**Package Manager**: uv 0.7.9+
