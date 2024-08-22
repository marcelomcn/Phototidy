#!/bin/bash

# Get the directory of the current script
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Change to the script's directory
cd "$SCRIPT_DIR"

# Run the Python script
python3 phototidy.py

