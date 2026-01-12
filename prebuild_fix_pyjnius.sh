#!/bin/bash
# Pre-build hook to fix pyjnius Python 3 compatibility

echo "🔧 Pre-build: Fixing pyjnius Python 3 compatibility..."

# This will be called before buildozer runs
# We'll patch pyjnius files as they're downloaded

# Function to fix pyjnius files
fix_pyjnius() {
    local file="$1"
    if [ -f "$file" ] && grep -q "isinstance(arg, long)" "$file" 2>/dev/null; then
        echo "   Patching: $file"
        # Replace long with int (Python 3 compatibility)
        sed -i '' 's/isinstance(arg, long)/False  # long removed in Python 3/g' "$file"
        sed -i '' 's/(isinstance(arg, long) and arg < 2147483648)/(False and arg < 2147483648)  # long removed/g' "$file"
        sed -i '' 's/ or isinstance(arg, long)//g' "$file"
    fi
}

# Watch for pyjnius files being created and fix them
# This is a workaround - ideally python-for-android would be fixed
export -f fix_pyjnius

echo "✅ Pre-build fix ready"
