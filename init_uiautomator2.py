"""
Simple script to initialize uiautomator2
Run this in Pydroid 3 to set up uiautomator2 (one time only)
"""

print("=" * 50)
print("uiautomator2 Initialization")
print("=" * 50)

try:
    import uiautomator2 as u2
    
    print("\n1. Connecting to device...")
    d = u2.connect()
    
    print("2. Getting device info (this initializes uiautomator2)...")
    info = d.info
    print(f"   ✅ Device: {info.get('productName', 'Unknown')}")
    print(f"   ✅ Screen: {info.get('displayWidth')}x{info.get('displayHeight')}")
    
    print("\n3. Testing connection...")
    current_app = d.app_current()
    print(f"   ✅ Current app: {current_app.get('package', 'Unknown')}")
    
    print("\n" + "=" * 50)
    print("✅ uiautomator2 is ready!")
    print("=" * 50)
    print("\nYou can now run android-automation.py")
    print("Make sure to grant all permissions when prompted!")
    
except ImportError:
    print("\n❌ uiautomator2 is not installed!")
    print("\nTo install:")
    print("1. Open Pydroid 3")
    print("2. Go to Pip menu")
    print("3. Install: uiautomator2")
    print("\nThen run this script again.")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure uiautomator2 is installed: pip install uiautomator2")
    print("2. Grant 'Display over other apps' permission")
    print("3. Try restarting your device")
    print("4. Make sure USB debugging is enabled (if using USB)")
