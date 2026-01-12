# Quick Setup Guide - Setup Wizard 🎯

## What is the Setup Wizard?

An **interactive tool** that helps you configure all coordinates and OCR regions by:
- Taking screenshots of your game
- Letting you visually select areas
- Testing coordinates
- Saving everything automatically

## How to Use

### Step 1: Run Setup Wizard

In Termux:
```bash
cd ~/storage/downloads
python3 setup_wizard.py
```

### Step 2: Follow the Prompts

The wizard will:
1. Take screenshots of your game
2. Ask you to set each coordinate
3. Let you select OCR regions
4. Test everything
5. Save to config file

### Step 3: Done!

The main script automatically uses the config. Just run:
```bash
python3 android-automation.py
```

## Getting Coordinates Easily

### Best Method: Use "Touch Coordinates" App

1. Install **"Touch Coordinates"** from Play Store (free)
2. Open it - shows X,Y as you tap
3. Tap where you want to click
4. Note the coordinates
5. Enter in wizard

### Alternative: Use Screenshot

1. Wizard takes screenshot
2. Open screenshot in gallery
3. Find the spot visually
4. Estimate coordinates (or use image viewer with coordinates)
5. Enter in wizard

## What You'll Configure

1. **Start click** - Where you click the car
2. **Button region** - Upgrade button area
3. **Reset clicks** - 3 reset button locations
4. **Post-timer clicks** - 2 clicks after timer
5. **OCR regions** - Where text appears (step numbers, amounts, timer)
6. **Thresholds** - Game settings (amounts, timer limits)

## Time Required

- **First time:** 10-15 minutes
- **If you need to adjust:** 5 minutes

## After Setup

Everything is saved to `automation_config.json`. The main script loads it automatically - no manual editing needed!

## Re-run Setup

Want to change something? Just run the wizard again - it will update the config.
