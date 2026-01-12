#!/bin/bash
# Script to find your downloaded files
# Run this in Termux to locate your files

echo "🔍 Searching for your files..."
echo ""

# Common download locations
SEARCH_PATHS=(
    "/sdcard/Download"
    "/sdcard/Downloads"
    "/storage/emulated/0/Download"
    "/storage/emulated/0/Downloads"
    "~/storage/downloads"
    "/sdcard"
)

FILES=("android-automation.py" "launcher.sh" "quick_start.sh" "run.sh" "setup_wizard.py")

FOUND=0

for file in "${FILES[@]}"; do
    echo "Looking for: $file"
    for path in "${SEARCH_PATHS[@]}"; do
        # Expand ~ if present
        expanded_path="${path/#\~/$HOME}"
        if [ -f "$expanded_path/$file" ]; then
            echo "  ✅ Found at: $expanded_path/$file"
            FOUND=1
            break
        fi
    done
    if [ $FOUND -eq 0 ]; then
        echo "  ❌ Not found in common locations"
    fi
    FOUND=0
    echo ""
done

echo "═══════════════════════════════════════════════════════"
echo "If files not found, try searching manually:"
echo ""
echo "To search entire phone (may take a while):"
echo "  find /sdcard -name 'android-automation.py' 2>/dev/null"
echo ""
echo "Or check Google Drive download folder:"
echo "  ls /sdcard/Android/data/com.google.android.apps.docs/files/"
echo ""
echo "Or check Termux downloads:"
echo "  ls ~/storage/downloads"
echo "═══════════════════════════════════════════════════════"
