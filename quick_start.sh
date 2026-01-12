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

# Install build dependencies for numpy
echo ""
echo "🔧 Installing build dependencies..."
pkg install -y binutils make gcc python-dev 2>/dev/null || true

# Install Python packages
echo ""
echo "📚 Installing Python packages..."
# Install packages one by one
python3 -m pip install --user pillow || echo "⚠️  Pillow had issues, continuing..."
python3 -m pip install --user numpy || {
    echo "⚠️  NumPy build failed, trying Termux package..."
    pkg install -y python-numpy 2>/dev/null || echo "⚠️  NumPy installation failed"
}
python3 -m pip install --user pytesseract || echo "⚠️  pytesseract had issues, continuing..."
python3 -m pip install --user uiautomator2 || echo "⚠️  uiautomator2 had issues"

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
