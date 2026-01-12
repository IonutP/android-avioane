# Android Automation Setup Guide for Pydroid 3

This guide will help you set up and run the automation script on your Android device using Pydroid 3.

## Prerequisites

1. **Pydroid 3** installed on your Android device
2. **ADB (Android Debug Bridge)** enabled on your device
3. **USB Debugging** enabled (or wireless ADB)

## Step 1: Enable Developer Options and USB Debugging

1. Go to **Settings** → **About Phone**
2. Tap **Build Number** 7 times to enable Developer Options
3. Go back to **Settings** → **Developer Options**
4. Enable **USB Debugging**
5. (Optional) Enable **Wireless Debugging** if you want to use ADB over WiFi

## Step 2: Install Required Python Packages

In Pydroid 3:

1. Open Pydroid 3
2. Tap the **Pip** menu (or go to Menu → Pip)
3. Install the following packages one by one:
   ```
   pillow
   numpy
   pytesseract
   ```
   
   **Note:** `opencv-python` is NOT required - the script uses free alternatives!
   
   OR use `easyocr` instead of `pytesseract`:
   ```
   easyocr
   ```

4. (Optional but recommended) Install `uiautomator2`:
   ```
   uiautomator2
   ```

## Step 3: Set Up ADB Connection

### Option A: USB Connection (Easier)

1. Connect your Android device to your computer via USB
2. On your computer, run:
   ```bash
   adb devices
   ```
3. Accept the USB debugging prompt on your phone
4. You should see your device listed

### Option B: Wireless ADB (No Computer Needed)

1. On your Android device, enable **Wireless Debugging** in Developer Options
2. Note the IP address and port (e.g., `192.168.1.100:5555`)
3. On another device or computer, connect:
   ```bash
   adb connect 192.168.1.100:5555
   ```

### Option C: Use ADB from Android Device (Advanced)

If you want to run ADB commands directly from your Android device:

1. Install **Termux** or similar terminal app
2. Install ADB in Termux:
   ```bash
   pkg install android-tools
   ```
3. Enable ADB over network in Developer Options
4. Connect to localhost:
   ```bash
   adb connect 127.0.0.1:5555
   ```

## Step 4: Configure the Script

Open `android-automation.py` in Pydroid 3 and adjust:

1. **Coordinates** - Update X/Y coordinates for your screen size:
   ```python
   self.start_click_x = 150
   self.start_click_y = 375
   # ... etc
   ```

2. **Thresholds** - Adjust game-specific values:
   ```python
   self.reset_target_amount = 10
   self.timer_threshold = 5
   self.amount_threshold = 20
   ```

3. **Delays** - Adjust timing:
   ```python
   self.click_delay = 1.0  # seconds
   ```

## Step 5: Run the Script

1. Open `android-automation.py` in Pydroid 3
2. Tap the **Run** button (▶️)
3. The script will:
   - Connect to your device
   - Take a screenshot to detect screen size
   - Start the automation

## Troubleshooting

### "uiautomator2 not available"
- The script will fall back to ADB commands
- Make sure ADB is accessible from your device
- Or install uiautomator2: `pip install uiautomator2`

### "ADB command failed"
- Make sure USB debugging is enabled
- Check that ADB can see your device: `adb devices`
- Try restarting ADB: `adb kill-server && adb start-server`

### "OCR not available"
- Install pytesseract: `pip install pytesseract`
- OR install easyocr: `pip install easyocr`
- Note: You may also need Tesseract OCR engine installed

### "Image processing libraries not available"
- Install: `pip install pillow numpy`
- **Note:** opencv-python is NOT needed - the script uses PIL/Pillow instead (free!)

### Screen coordinates are wrong
- Take a screenshot manually
- Use an image viewer to find the exact coordinates
- Update the coordinates in the script

### Script runs but doesn't click
- Check that the app you're automating is in the foreground
- Verify coordinates are correct for your screen size
- Make sure the device is not locked

## Alternative: Using uiautomator2 (Recommended)

If you install `uiautomator2`, it provides better automation:

1. Install: `pip install uiautomator2`
2. Initialize (run once):
   ```python
   import uiautomator2 as u2
   d = u2.connect()
   d.app_start("com.your.game.package")
   ```

## Notes

- The script saves screenshots to `/sdcard/automation_screenshots/`
- You can pause/resume by modifying the script (add pause button logic)
- Make sure the game/app is in the foreground when running
- Screen must stay on (disable screen timeout)

## Limitations

- Some features may not work perfectly on all Android devices
- OCR accuracy depends on screen quality and text clarity
- ADB commands require proper permissions
- Some devices may have restrictions on automation

## Support

If you encounter issues:
1. Check that all packages are installed correctly
2. Verify ADB connection works
3. Test with a simple click command first
4. Check device logs for errors
