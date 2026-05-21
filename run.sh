#!/bin/bash

# File Organizer - Linux/Mac Launcher
# This shell script sets up and runs the File Organizer on Linux/Mac

echo ""
echo "========================================"
echo "   FILE ORGANIZER - Linux/Mac Launcher"
echo "========================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3 using:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
    echo "  macOS: brew install python3"
    exit 1
fi

# Check Python version
python_version=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
echo "Python version: $python_version"

# Create logs directory if it doesn't exist
if [ ! -d "logs" ]; then
    mkdir -p logs
    echo "Created logs directory"
fi

# Check if schedule is installed, if not install it
echo ""
echo "Checking dependencies..."
python3 -c "import schedule" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing schedule library..."
    pip3 install schedule
fi

# Run setup verification
echo ""
echo "Running setup verification..."
python3 setup.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Setup verification failed. Please fix the issues above."
    exit 1
fi

# Run main application
echo ""
echo "Starting File Organizer..."
echo ""
python3 main.py
