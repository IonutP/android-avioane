# 🚀 Fresh Install Guide - Step by Step

Complete guide for installing the automation on a fresh Termux installation.

## Prerequisites

- Android device
- Termux installed from [F-Droid](https://f-droid.org/packages/com.termux/)
- Virtual Truck Manager 3 game installed on your device

## Fresh Install Steps

### Step 1: Open Termux

Open the Termux app on your Android device.

### Step 2: Grant Storage Permission

```bash
termux-setup-storage
```

When prompted, tap **"Allow"** to grant storage access.

### Step 3: Install wget

```bash
pkg update
pkg install -y wget
```

### Step 4: Download and Run Setup

```bash
cd ~/storage/downloads
wget -O download_and_setup.sh https://raw.githubusercontent.com/IonutP/android-avioane/main/download_and_setup.sh
bash download_and_setup.sh https://raw.githubusercontent.com/IonutP/android-avioane/main
```

This will:
- ✅ Download all required files
- ✅ Install Python (if needed)
- ✅ Install required packages (uiautomator2, pillow, numpy, pytesseract)
- ✅ Initialize uiautomator2 (you'll need to grant permissions)
- ✅ Run setup wizard to configure coordinates
- ✅ Start the automation

**That's it!** 🎉

---

## Alternative: Manual Download (If download script doesn't work)

If the download script doesn't work, you can manually download files:

```bash
cd ~/storage/downloads
mkdir -p android-avioane
cd android-avioane

# Download main files
wget https://raw.githubusercontent.com/IonutP/android-avioane/main/android-automation.py
wget https://raw.githubusercontent.com/IonutP/android-avioane/main/setup_wizard.py
wget https://raw.githubusercontent.com/IonutP/android-avioane/main/load_config.py
wget https://raw.githubusercontent.com/IonutP/android-avioane/main/run.sh
wget https://raw.githubusercontent.com/IonutP/android-avioane/main/launcher.sh

# Make scripts executable
chmod +x run.sh launcher.sh

# Run setup
bash run.sh
```

---

## What Happens During Setup

### 1. Python Installation
- If Python isn't installed, it will be installed automatically
- Takes ~1-2 minutes

### 2. Package Installation
- Installs: `uiautomator2`, `pillow`, `numpy`, `pytesseract`
- Takes ~10-20 minutes (depends on internet speed)
- **Be patient!** This is the longest step.

### 3. uiautomator2 Initialization
- Runs `python3 -m uiautomator2 init`
- **Important:** Grant all permissions when prompted:
  - Display over other apps
  - Accessibility service
  - Any other permissions requested

### 4. Setup Wizard
- If `automation_config.json` doesn't exist, the setup wizard will run
- You'll need to:
  - Take screenshots of your game
  - Set click coordinates
  - Set OCR regions
  - Configure thresholds

### 5. Automation Starts
- Once everything is configured, the automation will start
- Make sure Virtual Truck Manager 3 is ready!

---

## Daily Usage (After First Setup)

Once everything is set up, you can run the automation anytime:

```bash
cd ~/storage/downloads/android-avioane
bash run.sh
```

### Create a Shortcut (Optional)

Add this to your `~/.bashrc`:

```bash
echo 'alias autom8="cd ~/storage/downloads/android-avioane && bash run.sh"' >> ~/.bashrc
source ~/.bashrc
```

Then just type `autom8` to run!

---

## Troubleshooting

### "Permission denied" when running scripts

```bash
chmod +x run.sh
chmod +x download_and_setup.sh
```

### "Python not found"

The script should install it automatically, but if it fails:

```bash
pkg install -y python python-pip
```

### "uiautomator2 not found"

```bash
pip install uiautomator2
python3 -m uiautomator2 init
```

**Important:** Grant all permissions when prompted!

### "Package installation failed"

Check your internet connection:

```bash
ping -c 3 google.com
```

If internet works, try:

```bash
pip install --upgrade pip
pip install pillow numpy pytesseract uiautomator2
```

### Setup wizard doesn't work

Make sure:
- Virtual Truck Manager 3 is open and visible
- You grant all permissions when prompted
- Your device screen is on

### Files not found

Make sure you're in the right directory:

```bash
pwd  # Should show: /data/data/com.termux/files/home/storage/downloads/android-avioane
ls   # Should show: android-automation.py, run.sh, etc.
```

---

## File Locations

After installation, your files will be at:

```
/data/data/com.termux/files/home/storage/downloads/android-avioane/
├── android-automation.py    # Main script
├── run.sh                    # Launcher
├── setup_wizard.py          # Configuration wizard
├── automation_config.json    # Your configuration (created after setup)
└── ... (other files)
```

---

## Quick Reference

**First time setup:**
```bash
termux-setup-storage
pkg update && pkg install -y wget
cd ~/storage/downloads
wget -O download_and_setup.sh https://raw.githubusercontent.com/IonutP/android-avioane/main/download_and_setup.sh
bash download_and_setup.sh https://raw.githubusercontent.com/IonutP/android-avioane/main
```

**Daily use:**
```bash
cd ~/storage/downloads/automation
bash run.sh
```

---

## Need Help?

- Check other documentation files in the repository
- Make sure all permissions are granted
- Ensure Virtual Truck Manager 3 is installed and can be opened

---

**That's it!** You're ready to automate! 🚀
