#!/bin/bash

# Install the necessary tools
pip install pytest pyinstaller

# Run the tests
pytest test_calculator.py

# Create an executable
pyinstaller --onefile calculator.py