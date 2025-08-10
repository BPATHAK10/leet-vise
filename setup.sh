#!/bin/bash

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install requirements from requirements.txt
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate