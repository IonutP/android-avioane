#!/bin/bash
# Simple launcher script for Android Automation
# Makes it easy to run the automation - just double-tap or run: bash launcher.sh

clear
echo "╔═══════════════════════════════════════════════════════╗"
echo "║     Virtual Truck Manager 3 - Automation Launcher    ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python not found!"
    echo ""
    echo "Installing Python..."
    pkg install -y python python-pip
fi

# Check if pip is available
if ! command -v pip &> /dev/null; then
    echo "⚠️  pip not found - installing python-pip..."
    pkg install -y python-pip
fi

# Check if required packages are installed
echo "🔍 Checking dependencies..."
python3 -c "import uiautomator2" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  uiautomator2 not found!"
    echo ""
    echo "Installing required packages..."
    # Note: Don't upgrade pip in Termux - it breaks the python-pip package
    pip install uiautomator2 pillow numpy pytesseract
    echo ""
    echo "Initializing uiautomator2 (one time setup)..."
    python3 -m uiautomator2 init
    echo ""
fi

# Check if script exists
if [ ! -f "android-automation.py" ]; then
    echo "❌ android-automation.py not found!"
    echo ""
    echo "Make sure you're in the correct directory."
    echo "Current directory: $(pwd)"
    echo ""
    echo "To find the script, run:"
    echo "  find /sdcard -name 'android-automation.py' 2>/dev/null"
    exit 1
fi

echo "✅ Everything ready!"
echo ""
echo "═══════════════════════════════════════════════════════"
echo "Starting automation in 3 seconds..."
echo "Make sure Virtual Truck Manager 3 is ready!"
echo "═══════════════════════════════════════════════════════"
echo ""

sleep 3

# Run the automation script
python3 android-automation.py

# When script exits, show message
echo ""
echo "═══════════════════════════════════════════════════════"
echo "Automation stopped."
echo "Press any key to exit..."
read -n 1
clear
