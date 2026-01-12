#!/bin/bash
# Download and Setup Script
# Downloads all files from a URL and sets everything up
# Usage: bash download_and_setup.sh <base-url>
# Example: bash download_and_setup.sh https://raw.githubusercontent.com/yourusername/repo/main

# Default URL
DEFAULT_URL="https://raw.githubusercontent.com/IonutP/android-avioane/main"

BASE_URL="${1:-$DEFAULT_URL}"

# Check if wget is installed
if ! command -v wget &> /dev/null; then
    echo "📦 Installing wget..."
    pkg install -y wget
fi

echo "💡 Tip: You can specify a custom URL:"
echo "   bash download_and_setup.sh https://your-url.com"
echo ""

echo "╔═══════════════════════════════════════════════════════╗"
echo "║     Download and Setup - Virtual Truck Manager 3    ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Create downloads directory
# Note: Termux home is /data/data/com.termux/files/home
# After termux-setup-storage, ~/storage/downloads links to Downloads folder
mkdir -p ~/storage/downloads/automation
cd ~/storage/downloads/automation

echo "📥 Downloading files from: $BASE_URL"
echo ""

# List of files to download
FILES=(
    "android-automation.py"
    "setup_wizard.py"
    "load_config.py"
    "run.sh"
    "launcher.sh"
    "quick_start.sh"
)

# Download each file
DOWNLOADED=0
FAILED=0

for file in "${FILES[@]}"; do
    echo "📥 Downloading $file..."
    wget -q "$BASE_URL/$file" -O "$file"
    
    if [ $? -eq 0 ] && [ -f "$file" ]; then
        echo "   ✅ Downloaded $file"
        ((DOWNLOADED++))
        # Make scripts executable
        if [[ "$file" == *.sh ]]; then
            chmod +x "$file"
        fi
    else
        echo "   ❌ Failed to download $file"
        echo "   Make sure the URL is correct and file exists"
        ((FAILED++))
    fi
done

echo ""
echo "═══════════════════════════════════════════════════════"
if [ $DOWNLOADED -gt 0 ]; then
    echo "✅ Downloaded $DOWNLOADED file(s)"
    if [ $FAILED -gt 0 ]; then
        echo "⚠️  Failed to download $FAILED file(s)"
    fi
else
    echo "❌ Failed to download files!"
    echo "   Check the URL: $BASE_URL"
    echo "   Make sure you're using the correct GitHub repository URL"
    exit 1
fi
echo "═══════════════════════════════════════════════════════"
echo ""
echo "Current directory: $(pwd)"
echo ""
echo "🚀 Ready to run! Execute:"
echo "  bash run.sh"
echo ""
echo "The run.sh script will:"
echo "  - Check if setup is needed"
echo "  - Install packages if needed"
echo "  - Run setup wizard if needed"
echo "  - Start automation"
echo ""
read -p "Press Enter to run automation now, or Ctrl+C to exit..."
bash run.sh
