#!/bin/bash
#
# Batch mode runner for PyTecplot scripts
# 
# This script activates the virtual environment and configures the Tecplot
# environment for fast batch mode execution (without connecting to the GUI).
#
# Usage:
#   ./run_batch.sh src/hello_world.py
#   ./run_batch.sh src/apply_zone_styles.py arg1 arg2
#
# Batch mode is significantly faster than connected mode because PyTecplot
# directly interfaces with the Tecplot engine libraries rather than
# communicating with the Tecplot GUI through sockets.

set -e  # Exit on error

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate virtual environment
source "$SCRIPT_DIR/.venv/bin/activate"

# Run the script with tec360-env for batch mode
# The tec360-env script sets up the correct environment variables for
# the Tecplot 360 engine to run in batch mode.
# Point the below path to your Tecplot 360 installation directory.
"/Applications/Tecplot 360 EX 2025 R1/bin/tec360-env" -- python "$@"
