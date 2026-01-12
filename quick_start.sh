#!/bin/bash
# Quick Start - One-time setup script
# Run this ONCE to set everything up

clear
echo "╔═══════════════════════════════════════════════════════╗"
echo "║        Android Automation - Quick Setup              ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Request storage permission
echo "📁 Requesting storage permission..."
termux-setup-storage

# Update packages
echo ""
echo "📦 Updating packages (this may take a few minutes)..."
pkg update -y && pkg upgrade -y

# Install Python
echo ""
echo "🐍 Installing Python..."
pkg install -y python python-pip

# Install Python packages
echo ""
echo "📚 Installing Python packages..."
# Note: Don't upgrade pip in Termux - it breaks the python-pip package
pip install pillow numpy pytesseract uiautomator2

# Initialize uiautomator2
echo ""
echo "🔧 Initializing uiautomator2..."
echo "   ⚠️  Grant permissions when prompted!"
echo "   - Display over other apps"
echo "   - Accessibility (if asked)"
echo ""
python3 -m uiautomator2 init

echo ""
echo "═══════════════════════════════════════════════════════"
echo "✅ Setup Complete!"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "Next steps:"
echo "1. Copy android-automation.py to your phone"
echo "2. Copy launcher.sh to the same folder"
echo "3. In Termux, navigate to that folder:"
echo "   cd /sdcard/Download  # or wherever you saved files"
echo "4. Make launcher executable:"
echo "   chmod +x launcher.sh"
echo "5. Run the launcher:"
echo "   ./launcher.sh"
echo ""
echo "Or simply: bash launcher.sh"
echo ""
echo "That's it! 🎉"
