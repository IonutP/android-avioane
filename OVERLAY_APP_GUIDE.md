# Overlay App Guide - Clicker-Style Automation 📱

This app runs as a floating overlay on top of your game, just like clicker apps!

## Features

✅ **Floating Overlay** - Runs on top of the game  
✅ **Tap to Set Coordinates** - Just tap where you want to click  
✅ **Draw OCR Regions** - Touch and drag to create rectangles  
✅ **Visual Feedback** - See rectangles and click points on screen  
✅ **Save/Load Config** - Save your setup  
✅ **Run Automation** - Start automation from overlay  

## How It Works

1. **Install the APK** on your device or BlueStacks
2. **Grant Overlay Permission** when prompted
3. **Open your game** (Virtual Truck Manager 3)
4. **Tap the gear icon (⚙️)** to open the overlay menu
5. **Set up coordinates and OCR regions** by tapping/drawing
6. **Run automation** - it clicks on top of the game!

## Setup Steps

### Step 1: Build the APK

Follow `BUILD_APK_GUIDE.md` to build the APK.

### Step 2: Install on Device/BlueStacks

1. Transfer APK to device or drag into BlueStacks
2. Install the APK
3. **Grant Overlay Permission**:
   - Settings → Apps → Special Access → Display over other apps
   - Find "Game Automation" and enable it

### Step 3: Configure

1. **Open your game**
2. **Open the overlay app** (it will appear as a floating button)
3. **Tap the gear icon (⚙️)** to open controls

### Step 4: Set Click Points

1. Tap **"Set Click Point"**
2. **Tap on the game screen** where you want to click
3. A yellow circle appears showing the coordinate
4. Repeat for all click points

### Step 5: Draw OCR Regions

1. Tap **"Draw OCR Region"**
2. **Touch and drag** on the game screen to draw a rectangle
3. The rectangle shows where OCR will read text
4. Repeat for all OCR regions (button text, timer, etc.)

### Step 6: Save and Run

1. Tap **"Save Config"** to save your setup
2. Tap **"Run Automation"** to start
3. The automation will click on top of the game!

## Using in BlueStacks

1. **Install BlueStacks** on your computer
2. **Install the APK** in BlueStacks:
   - Drag APK into BlueStacks window, or
   - Use: `adb install gameautomation.apk`
3. **Enable Overlay Permission** in BlueStacks settings
4. **Open your game** in BlueStacks
5. **Open overlay app** - it floats on top!
6. **Configure and run** as described above

## Controls

- **⚙️ Button** - Toggle control panel
- **Draw OCR Region** - Touch and drag to create rectangle
- **Set Click Point** - Tap to set coordinate
- **Save Config** - Save your setup
- **Load Config** - Load saved setup
- **Run Automation** - Start automation
- **Clear Rectangles** - Remove all drawn rectangles

## Visual Feedback

- **Yellow Circle** - Click point
- **Green Rectangle** - OCR region
- **Red Rectangle** - Currently drawing rectangle
- **Semi-transparent Background** - Overlay area

## Tips

1. **Position the overlay button** where it won't block game elements
2. **Draw OCR regions** around text you want to read
3. **Test click points** before running automation
4. **Save config** frequently as you adjust
5. **Use BlueStacks** for easier testing and debugging

## Troubleshooting

### Overlay doesn't appear
- Check overlay permission is granted
- Restart the app
- Check if another overlay app is blocking it

### Can't draw rectangles
- Make sure you tapped "Draw OCR Region" first
- Try again - touch and drag slowly

### Click points not working
- Make sure coordinates are set correctly
- Check that the game is in the foreground
- Verify automation has necessary permissions

### App crashes
- Check that all dependencies are installed
- Rebuild the APK
- Check device/BlueStacks compatibility

## Next Steps

Once the overlay is working:

1. **Test in BlueStacks** first
2. **Fine-tune coordinates** by tapping and testing
3. **Adjust OCR regions** to capture text correctly
4. **Run automation** and monitor results
5. **Save working config** for future use

The overlay makes it super easy to set up - just tap and draw! 🎯
