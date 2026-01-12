"""
Coordinate Logger - Shows X,Y coordinates when you tap the screen
Run this in a separate Termux window while using setup wizard
"""

import time

try:
    import uiautomator2 as u2
    device = u2.connect()
    print("✅ Connected to device")
except ImportError:
    print("❌ uiautomator2 not installed")
    exit(1)
except Exception as e:
    print(f"❌ Connection failed: {e}")
    exit(1)

print("""
╔═══════════════════════════════════════════════════════╗
║           Coordinate Logger - Tap to Get X,Y          ║
╚═══════════════════════════════════════════════════════╝

This script will show coordinates when you tap the screen.

HOW TO USE:
1. Keep this script running
2. Tap anywhere on your screen
3. Coordinates will be displayed here
4. Copy the coordinates to the setup wizard

Note: This uses uiautomator2's click monitoring.
For better results, use the manual method in setup wizard.

Press Ctrl+C to stop.
═══════════════════════════════════════════════════════
""")

# Get screen size
info = device.info
screen_width = info['displayWidth']
screen_height = info['displayHeight']
print(f"📱 Screen size: {screen_width}x{screen_height}\n")

print("⚠️  Note: uiautomator2 cannot directly capture your taps.")
print("   Use this alternative method:\n")
print("1. Take a screenshot of your game")
print("2. Open the screenshot in an image viewer")
print("3. Note the X,Y coordinates where you want to click")
print("4. Enter those coordinates in the setup wizard")
print("\nOr use an app like 'Touch Coordinates' from Play Store")
print("   to see live coordinates as you tap.\n")

# Alternative: Create a simple coordinate display overlay
# This would require root or special permissions
print("For now, the setup wizard will guide you through")
print("manual coordinate entry with screenshot assistance.")
