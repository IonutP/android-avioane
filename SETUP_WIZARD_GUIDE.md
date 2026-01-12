# Setup Wizard Guide - Visual Coordinate Setup 🎯

The setup wizard makes it easy to configure all coordinates and OCR regions by using screenshots and visual selection.

## How It Works

1. **Takes screenshots** of your game
2. **You view the screenshots** to find coordinates
3. **You enter coordinates** (or use a coordinate app)
4. **Wizard marks regions** on screenshots so you can verify
5. **Saves everything** to a config file automatically

## Quick Start

### Step 1: Run the Setup Wizard

In Termux:
```bash
cd ~/storage/downloads
python3 setup_wizard.py
```

### Step 2: Follow the Prompts

The wizard will guide you through:
1. Setting click coordinates (start click, reset clicks, etc.)
2. Selecting OCR regions (draw rectangles on screenshots)
3. Setting game thresholds
4. Testing coordinates

### Step 3: Use the Config

The wizard saves everything to `automation_config.json`. The main script automatically loads it!

## Getting Coordinates

### Method 1: Use Screenshot + Manual Entry (Easiest)

1. Wizard takes a screenshot
2. Open screenshot in your gallery
3. Note the X,Y coordinates where you want to click
4. Enter them when prompted

### Method 2: Use a Coordinate App (Recommended)

Install **"Touch Coordinates"** or similar from Play Store:
1. Open the app
2. It shows X,Y coordinates as you tap
3. Tap where you want to click
4. Note the coordinates
5. Enter them in the wizard

### Method 3: Use Image Viewer with Coordinates

Some image viewers show coordinates when you tap:
1. Open screenshot in image viewer
2. Tap to see coordinates
3. Note them down
4. Enter in wizard

## Selecting OCR Regions

For OCR regions (rectangles):

1. **Wizard takes screenshot**
2. **Open screenshot** in gallery
3. **Find the area** where text appears (like "10/20" or amount)
4. **Note the coordinates:**
   - Top-left corner (X, Y)
   - Width and height
5. **Enter them** when prompted
6. **Wizard marks the region** on screenshot (red rectangle)
7. **Verify it's correct**

## Example Workflow

```
1. Run: python3 setup_wizard.py
2. Wizard: "Taking screenshot..."
3. You: Open screenshot, find where to click
4. You: Note coordinates (e.g., 150, 375)
5. Wizard: "Enter X coordinate:"
6. You: Enter 150
7. Wizard: "Enter Y coordinate:"
8. You: Enter 375
9. Wizard: "Test click? (y/n)"
10. You: y (to verify)
11. Repeat for all coordinates
```

## Tips

### Tip 1: Use Touch Coordinates App
- Install from Play Store
- Shows live X,Y as you tap
- Makes coordinate entry super easy

### Tip 2: Take Multiple Screenshots
- Wizard takes screenshots at each step
- Open them to see exactly where things are
- Use them as reference

### Tip 3: Test Each Coordinate
- Wizard asks if you want to test
- Say "y" to test each click
- Verify it clicks the right place

### Tip 4: Verify OCR Regions
- Wizard marks selected regions in red
- Open the marked screenshot
- Make sure the red rectangle covers the text area

## What Gets Saved

The wizard creates `automation_config.json` with:
- All click coordinates
- All OCR regions
- Game thresholds
- Everything needed for automation

## After Setup

Once setup is complete:

1. **Config is saved** automatically
2. **Main script loads it** automatically
3. **Just run:** `python3 android-automation.py`
4. **Everything works!**

## Re-running Setup

Want to change coordinates?

1. Run setup wizard again
2. It will overwrite the old config
3. Or edit `automation_config.json` manually

## Troubleshooting

### "Can't see coordinates in screenshot"
- Use "Touch Coordinates" app instead
- Or use an image viewer that shows coordinates

### "Region selection is wrong"
- Wizard shows marked screenshot
- Check the red rectangle
- If wrong, say "n" and try again

### "Test click doesn't work"
- Make sure game is in foreground
- Check coordinates are correct
- Try again with different coordinates

## Summary

**Setup Wizard = Easy visual configuration!**

1. Takes screenshots
2. You find coordinates (using app or manually)
3. Enter coordinates
4. Wizard saves everything
5. Done! 🎉
