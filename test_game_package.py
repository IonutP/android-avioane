"""
Test script to find your game package name
Run this in Pydroid 3 while your game is open
"""

print("=" * 50)
print("Finding Game Package Name")
print("=" * 50)
print("\n⚠️  Make sure your game is OPEN before running this!")
print("Press Enter when ready, or wait 3 seconds...")
print()

import time
time.sleep(3)

try:
    import uiautomator2 as u2
    
    print("Connecting to device...")
    d = u2.connect()
    
    print("Getting current app info...")
    current = d.app_current()
    
    print("\n" + "=" * 50)
    print("Current App Information:")
    print("=" * 50)
    print(f"Package Name: {current.get('package', 'Unknown')}")
    print(f"Activity: {current.get('activity', 'Unknown')}")
    print("\nFull info:")
    print(current)
    
    package = current.get('package', '')
    if package:
        print("\n" + "=" * 50)
        print(f"✅ Your game package: {package}")
        print("=" * 50)
        print(f"\nCopy this to android-automation.py:")
        print(f'GAME_PACKAGE = "{package}"')
    else:
        print("\n⚠️  Could not detect package name")
        print("Make sure the game is in the foreground")
        
except ImportError:
    print("\n❌ uiautomator2 is not installed!")
    print("Install it first: pip install uiautomator2")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nMake sure:")
    print("1. Your game is open and in the foreground")
    print("2. uiautomator2 is installed and initialized")
    print("3. All permissions are granted")
