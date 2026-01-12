# Termux Setup - Much Easier! 📱

Termux is a **terminal emulator** for Android that's much easier to use than Pydroid 3 for automation scripts.

## Why Termux is Better

- ✅ **Easier package installation** - Just use `pip install`
- ✅ **Better terminal** - Full Linux terminal experience
- ✅ **No premium required** - Everything is free
- ✅ **Better for automation** - Designed for command-line tools
- ✅ **More reliable** - Better package management

## ⚡ Quick Setup (5 minutes) - EASIEST METHOD!

### Step 1: Install Termux

1. Download **Termux** from [F-Droid](https://f-droid.org/packages/com.termux/) (recommended)
2. Open Termux

### Step 2: Run Automated Setup

1. **Copy `quick_start.sh` to your phone** (Downloads folder)
2. In Termux, run:
   ```bash
   cd /sdcard/Download
   bash quick_start.sh
   ```
3. **Grant permissions** when prompted
4. Wait for setup to complete (5-10 minutes)

**That's it!** Setup is automated! ✅

### Alternative: Manual Setup

If you prefer manual setup, run these commands:

```bash
# Update packages
pkg update && pkg upgrade

# Install Python
pkg install python python-pip

# Install Python packages
pip install pillow numpy pytesseract uiautomator2

# Initialize uiautomator2 (one time)
python3 -m uiautomator2 init
```

### Step 3: Copy Scripts to Your Phone

Copy these files to your phone (Downloads folder):
- `android-automation.py` (main script)
- `launcher.sh` (easy launcher - makes it simple to run)

### Step 4: Run the Automation!

**Easy way (recommended):**
```bash
cd /sdcard/Download
bash launcher.sh
```

The launcher will:
- ✅ Check everything is installed
- ✅ Auto-install missing packages
- ✅ Run the automation
- ✅ Show helpful messages

**Or run directly:**
```bash
cd /sdcard/Download
python3 android-automation.py
```

That's it! Much simpler than Pydroid 3! 🎉

## Daily Usage

1. Open Termux
2. Navigate to script folder: `cd /path/to/script`
3. Run: `python android-automation.py`
4. Done!

## Troubleshooting

### "Command not found"
- Make sure you ran `pkg install python python-pip`

### "Permission denied"
- Grant Termux storage permission: `termux-setup-storage`
- Grant uiautomator2 permissions when prompted

### "uiautomator2 not found"
- Run: `pip install uiautomator2`
- Then: `python -m uiautomator2 init`

## Benefits Over Pydroid 3

- ✅ No premium features needed
- ✅ Easier package management
- ✅ Better terminal experience
- ✅ More reliable
- ✅ Can run in background
- ✅ Better for automation scripts
