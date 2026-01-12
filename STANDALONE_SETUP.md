# Standalone Setup - No Computer Needed! 📱

This guide shows you how to run the automation script **completely on your Android device** without needing a computer.

## ✅ Requirements

1. **Pydroid 3** installed
2. **uiautomator2** (REQUIRED for standalone operation)
3. Python packages: pillow, numpy, pytesseract (or easyocr)

## 🚀 Step-by-Step Setup

### Step 1: Install Python Packages

In Pydroid 3:

1. Open **Pip** menu
2. Install these packages:
   ```
   pillow
   numpy
   pytesseract
   uiautomator2
   ```

### Step 2: Initialize uiautomator2 (ONE TIME ONLY)

This is the most important step! uiautomator2 needs to install a helper app on your device.

**Method 1: Using Pydroid 3 (Easiest)**

1. **In Pydroid 3**, create a NEW Python file (tap + button)
2. **Copy and paste this code:**
   ```python
   import uiautomator2 as u2
   d = u2.connect()
   print("Initializing uiautomator2...")
   print(d.info)  # This will trigger initialization
   ```
3. **Tap the Run button (▶️)** in Pydroid 3
4. **Grant permissions** when prompted:
   - Allow "Display over other apps" permission
   - Allow "Accessibility service" if prompted
   - Allow any other permissions requested
5. You should see device information printed

**Method 2: Using Terminal in Pydroid 3**

1. In Pydroid 3, tap the **Terminal** button (or Menu → Terminal)
2. Type this command and press Enter:
   ```
   python -m uiautomator2 init
   ```
3. **Grant permissions** when prompted

**Verify it works:**

Create a new file in Pydroid 3 and run:
```python
import uiautomator2 as u2
d = u2.connect()
print(d.info)  # Should print device info
```

If you see device information, it's working! ✅

### Step 3: Find Your Game Package Name

**Method 1: Using uiautomator2 (Easiest)**

1. **Open your game** (Virtual Truck Manager 3)
2. **In Pydroid 3**, create a NEW Python file
3. **Copy and paste this code:**
   ```python
   import uiautomator2 as u2
   d = u2.connect()
   print(d.app_current())
   ```
4. **Tap Run (▶️)** in Pydroid 3
5. Look for the `package` field in the output - that's your game package name!

**Note:** Your game package is already set: `com.virtualtruck.manager3` ✅

**Method 2: Using Package Name Viewer App**

1. Install "Package Name Viewer" from Play Store
2. Open it and find your game
3. Copy the package name

**Method 3: Manual Method**

1. Open your game
2. The package name is usually: `com.companyname.gamename`
3. You can also check in Play Store URL or app settings

### Step 4: Configure the Script

1. Open `android-automation.py` in Pydroid 3
2. Find this line near the bottom:
   ```python
   GAME_PACKAGE = None  # <-- SET THIS TO YOUR GAME PACKAGE NAME
   ```
3. Change it to your game's package name:
   ```python
   GAME_PACKAGE = "com.your.game.package"  # Replace with actual package name
   ```

### Step 5: Run the Script!

1. **Open Pydroid 3**
2. **Open `android-automation.py`**
3. **Tap the Run button (▶️)**
4. The script will:
   - Connect to your device (standalone, no computer!)
   - Automatically open your game
   - Start automation immediately

## 🎯 How It Works

The script uses **uiautomator2** which:
- ✅ Works completely standalone (no computer needed)
- ✅ Can open apps automatically
- ✅ Can take screenshots
- ✅ Can click on coordinates
- ✅ All without ADB or computer connection!

## 🔧 Troubleshooting

### "uiautomator2 connection failed"

**Solution:**
1. Make sure uiautomator2 is initialized:
   ```python
   python -m uiautomator2 init
   ```
2. Grant all permissions when prompted
3. Try restarting your device

### "Could not open game"

**Solution:**
1. Verify the package name is correct
2. Make sure the game is installed
3. Try opening the game manually first, then run the script

### "Click failed" or "Screenshot failed"

**Solution:**
1. Make sure uiautomator2 is properly initialized
2. Grant "Display over other apps" permission
3. Check that the game is in the foreground

### Script runs but game doesn't open

**Solution:**
1. Set the game package name correctly
2. Make sure the game is installed
3. Try opening the game manually, then quickly run the script

## 💡 Tips

1. **Keep Screen On**: Set screen timeout to 30 minutes or "Never" while charging
2. **Disable Battery Optimization**: For Pydroid 3 in Settings → Battery
3. **Grant Permissions**: Make sure all permissions are granted for uiautomator2
4. **Test First**: Run a simple test to verify uiautomator2 works:
   ```python
   import uiautomator2 as u2
   d = u2.connect()
   d.click(500, 500)  # Test click
   ```

## 🎉 Benefits of Standalone Mode

- ✅ **No computer needed** - Run everything on your phone
- ✅ **Automatic game opening** - Script opens the game for you
- ✅ **Works anywhere** - No USB cable or WiFi ADB needed
- ✅ **Simple setup** - Just initialize uiautomator2 once
- ✅ **Reliable** - Uses Android's built-in automation framework

## 📝 Quick Start Checklist

- [ ] Installed pillow, numpy, pytesseract, uiautomator2 in Pydroid 3
- [ ] Initialized uiautomator2: `python -m uiautomator2 init`
- [ ] Granted all permissions
- [ ] Found game package name
- [ ] Set GAME_PACKAGE in script
- [ ] Tested uiautomator2 connection
- [ ] Ready to run!

Enjoy your fully standalone automation! 🚀
