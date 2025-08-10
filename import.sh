#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Install requirements from requirements.txt
python main.py --import-data

# Deactivate the virtual environment
deactivate