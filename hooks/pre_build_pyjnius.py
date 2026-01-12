#!/usr/bin/env python3
"""
Pre-build hook to fix pyjnius Python 3 compatibility issue.
This hook patches jnius_utils.pxi files to remove 'long' type references.
"""

import os
import glob
import re

def patch_pyjnius_files():
    """Find and patch all jnius_utils.pxi files."""
    # Find all jnius_utils.pxi files in .buildozer directory
    pattern = os.path.join('.buildozer', '**', 'jnius_utils.pxi')
    files = glob.glob(pattern, recursive=True)
    
    patched = 0
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Replace isinstance(arg, long) with isinstance(arg, int)
            content = re.sub(
                r'isinstance\(arg,\s*long\)',
                'isinstance(arg, int)',
                content
            )
            
            # Replace (isinstance(arg, long) and ...) with (isinstance(arg, int) and ...)
            content = re.sub(
                r'\(isinstance\(arg,\s*long\)\s+and',
                '(isinstance(arg, int) and',
                content
            )
            
            # Remove " or isinstance(arg, long)" patterns
            content = re.sub(
                r'\s+or\s+isinstance\(arg,\s*long\)',
                '',
                content
            )
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Patched: {filepath}")
                patched += 1
        except Exception as e:
            print(f"⚠️  Error patching {filepath}: {e}")
    
    if patched > 0:
        print(f"✅ Fixed {patched} pyjnius file(s)")
    return patched > 0

if __name__ == '__main__':
    patch_pyjnius_files()
