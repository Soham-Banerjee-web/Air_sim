#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")/.."

# Activate the virtual environment if needed
# source venv/bin/activate

# Run the simulation
python -m src.sim.simulation