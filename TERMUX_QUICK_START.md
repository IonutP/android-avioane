# Termux Quick Start Guide - Super Easy! 🚀

This is the **easiest way** to run the automation on Android - no building, no complex setup!

## ⚡ Quick Setup (5 minutes)

### Step 1: Install Termux

1. Download **Termux** from [F-Droid](https://f-droid.org/packages/com.termux/) (recommended)
   - Or from Google Play Store (may be older version)
2. Open Termux

### Step 2: Run Setup Script

1. **Copy `quick_start.sh` to your phone** (to Downloads folder)
2. In Termux, run:
   ```bash
   cd /sdcard/Download
   bash quick_start.sh
   ```
3. **Grant permissions** when prompted:
   - Storage permission
   - Display over other apps (for uiautomator2)
   - Any other permissions requested

**That's it!** Setup is done! ✅

### Step 3: Copy Scripts to Your Phone

1. Copy these files to your phone (Downloads folder):
   - `android-automation.py`
   - `launcher.sh`

### Step 4: Run the Automation!

In Termux:
```bash
cd /sdcard/Download
bash launcher.sh
```

**That's it!** The script will:
- Check everything is installed
- Start the automation
- Open your game automatically
- Begin clicking!

## 📱 Daily Usage (Super Simple!)

1. **Open Termux**
2. **Type:** `cd /sdcard/Download && bash launcher.sh`
3. **Done!** Automation starts

### Even Easier: Create a Shortcut

You can create a Termux widget or shortcut:

1. Long-press Termux icon
2. Create widget/shortcut
3. Set command: `cd /sdcard/Download && bash launcher.sh`
4. Now just tap the shortcut!

## 🎯 What the Launcher Does

The `launcher.sh` script:
- ✅ Checks if Python is installed
- ✅ Checks if packages are installed
- ✅ Installs missing packages automatically
- ✅ Runs the automation script
- ✅ Shows helpful messages

**You just run one command!**

## 📂 File Structure

After setup, you should have:
```
/sdcard/Download/
  ├── android-automation.py  (main script)
  ├── launcher.sh            (easy launcher)
  └── quick_start.sh         (setup script - run once)
```

## 🔧 Troubleshooting

### "Permission denied"
```bash
chmod +x launcher.sh
```

### "Python not found"
The launcher will install it automatically, or run:
```bash
pkg install python
```

### "uiautomator2 not found"
The launcher will install it automatically, or run:
```bash
pip install uiautomator2
python3 -m uiautomator2 init
```

### Script not found
Make sure you're in the right directory:
```bash
cd /sdcard/Download
ls  # Should show android-automation.py
```

## 💡 Pro Tips

### Tip 1: Create an Alias

Add this to `~/.bashrc` in Termux:
```bash
alias autom8='cd /sdcard/Download && bash launcher.sh'
```

Then just type `autom8` to run!

### Tip 2: Run in Background

```bash
nohup bash launcher.sh &
```

### Tip 3: Keep Screen On

In Termux, run:
```bash
termux-wake-lock
```

This keeps screen on while script runs.

## ✅ Advantages Over Pydroid 3

- ✅ **Easier setup** - Just run one script
- ✅ **Better terminal** - Full Linux experience
- ✅ **Auto-install** - Launcher installs missing packages
- ✅ **No premium** - Everything free
- ✅ **More reliable** - Better package management
- ✅ **Can run in background** - Keep using your phone

## 🎉 Summary

1. Install Termux
2. Run `quick_start.sh` (once)
3. Copy scripts to phone
4. Run `launcher.sh` (every time)

**That's it!** Much simpler than Pydroid 3! 🚀
