# Complete Setup Guide - Brand New Device 📱

Step-by-step guide to set up automation on a completely new Android device.

## Prerequisites

- Android device (phone or tablet)
- Internet connection (WiFi recommended)
- 30-45 minutes for initial setup

## Step-by-Step Setup

### Step 1: Install Termux (5 minutes)

1. **Download Termux:**
   - Go to [F-Droid](https://f-droid.org/packages/com.termux/) (recommended)
   - Or Google Play Store (may be older version)
   - Install the app

2. **Open Termux**
   - Grant any initial permissions if asked

### Step 2: Set Up Storage Access (1 minute)

In Termux, run:
```bash
termux-setup-storage
```

**Important:** When permission dialog appears, tap **"Allow"**

This gives Termux access to your phone's storage.

### Step 3: Transfer Files to Your Phone (2 minutes)

**Option A: USB Cable (Fastest)**
1. Connect phone to computer via USB
2. Select "File Transfer" mode on phone
3. Copy these files to phone's **Downloads** folder:
   - `android-automation.py`
   - `setup_wizard.py`
   - `load_config.py`
   - `launcher.sh`
   - `quick_start.sh`

**Option B: Google Drive**
1. Upload files to Google Drive from computer
2. On phone, open Google Drive app
3. Download files to Downloads folder

**Option C: Email**
1. Email files to yourself
2. Open email on phone
3. Download attachments

### Step 4: Run One-Time Setup (10-20 minutes)

In Termux:
```bash
cd ~/storage/downloads
bash quick_start.sh
```

**What this does:**
- Updates Termux packages
- Installs Python
- Installs required packages (pillow, numpy, pytesseract, uiautomator2)
- Initializes uiautomator2

**Time:** 10-20 minutes (depends on internet speed)

**Important:** 
- Keep Termux open during installation
- Grant permissions when prompted
- Be patient - numpy takes the longest!

### Step 5: Run Setup Wizard (10-15 minutes)

Once setup is complete, configure your coordinates:

```bash
python3 setup_wizard.py
```

**What you'll do:**
1. Open Virtual Truck Manager 3
2. Wizard takes screenshots
3. You set coordinates by:
   - Using "Touch Coordinates" app (recommended)
   - Or viewing screenshots and entering coordinates
4. Select OCR regions (draw rectangles)
5. Set game thresholds
6. Test coordinates

**Tips:**
- Install "Touch Coordinates" app from Play Store (free)
- It shows X,Y as you tap - makes it super easy!
- Take your time - accuracy is important

### Step 6: Run Automation! (Ready to go!)

```bash
bash launcher.sh
```

Or:
```bash
python3 android-automation.py
```

**That's it!** Automation starts automatically! 🎉

## Quick Reference

### Daily Usage (After Setup)

1. Open Termux
2. Run: `cd ~/storage/downloads && bash launcher.sh`
3. Done!

### Files You Need

Make sure these are in `~/storage/downloads`:
- ✅ `android-automation.py` (main script)
- ✅ `setup_wizard.py` (configuration)
- ✅ `load_config.py` (config loader)
- ✅ `launcher.sh` (easy launcher)
- ✅ `quick_start.sh` (setup - run once)

### Troubleshooting

**"Permission denied"**
```bash
termux-setup-storage
# Grant permission when prompted
```

**"File not found"**
```bash
cd ~/storage/downloads
ls  # Check if files are there
```

**"uiautomator2 not found"**
```bash
pip install uiautomator2
python3 -m uiautomator2 init
```

**"Python not found"**
```bash
pkg install python
```

## Complete Checklist

- [ ] Termux installed
- [ ] Storage permission granted (`termux-setup-storage`)
- [ ] Files copied to Downloads folder
- [ ] One-time setup completed (`bash quick_start.sh`)
- [ ] uiautomator2 initialized (permissions granted)
- [ ] Setup wizard completed (`python3 setup_wizard.py`)
- [ ] Config file created (`automation_config.json`)
- [ ] Tested coordinates work
- [ ] Ready to automate!

## Time Breakdown

- **Termux install:** 5 minutes
- **File transfer:** 2 minutes
- **One-time setup:** 10-20 minutes
- **Setup wizard:** 10-15 minutes
- **Total:** ~30-45 minutes (one time only!)

## After Setup

Everything is saved! Next time you just:
1. Open Termux
2. Run: `bash launcher.sh`
3. Automation starts!

No more setup needed! 🎉
