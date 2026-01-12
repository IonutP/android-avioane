#!/bin/bash
# Fix pyjnius Python 3 compatibility issue

echo "🔧 Fixing pyjnius Python 3 compatibility..."

# Find all jnius_utils.pxi files
find .buildozer -name "jnius_utils.pxi" -type f 2>/dev/null | while read file; do
    if grep -q "isinstance(arg, long)" "$file" 2>/dev/null; then
        echo "   Fixing: $file"
        # Replace all instances of long with int (Python 3 compatibility)
        # Fix: isinstance(arg, long) -> isinstance(arg, int)
        sed -i '' 's/isinstance(arg, long)/isinstance(arg, int)/g' "$file"
        # Fix: (isinstance(arg, long) and ...) -> (isinstance(arg, int) and ...)
        sed -i '' 's/(isinstance(arg, long) and/(isinstance(arg, int) and/g' "$file"
        # Fix: or isinstance(arg, long) -> (remove, int already checked)
        sed -i '' 's/ or isinstance(arg, long)//g' "$file"
    fi
done

echo "✅ Fixed pyjnius files"
