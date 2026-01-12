# 🚀 START HERE - Complete Setup for New Device

## Quick Start (30-45 minutes total)

### 1️⃣ Install Termux (5 min)
- Download from [F-Droid](https://f-droid.org/packages/com.termux/)
- Open Termux

### 2️⃣ Grant Storage Permission (1 min)
```bash
termux-setup-storage
```
Tap "Allow" when prompted

### 3️⃣ Copy Files to Phone (2 min)
Copy these to your phone's **Downloads** folder:
- `android-automation.py`
- `setup_wizard.py`
- `load_config.py`
- `launcher.sh`
- `quick_start.sh`

### 4️⃣ Run Setup (10-20 min)
In Termux:
```bash
cd ~/storage/downloads
bash quick_start.sh
```
Wait for installation to complete (be patient!)

### 5️⃣ Configure Coordinates (10-15 min)
```bash
python3 setup_wizard.py
```
Follow the wizard to set all coordinates

### 6️⃣ Run Automation! 🎉
```bash
bash run.sh
```

**OR use the smart launcher (recommended):**
```bash
bash run.sh
```

The smart launcher (`run.sh`) automatically:
- ✅ Checks if setup is needed
- ✅ Runs setup if needed
- ✅ Runs automation if ready
- ✅ One script does everything!

## That's It!

After setup, daily usage is just:
```bash
cd ~/storage/downloads && bash launcher.sh
```

## Need Help?

- See `COMPLETE_SETUP_GUIDE.md` for detailed steps
- See `TERMUX_QUICK_START.md` for Termux-specific help
- See `SETUP_WIZARD_GUIDE.md` for coordinate setup help

## Pro Tip

Install **"Touch Coordinates"** app from Play Store - it shows X,Y as you tap, making coordinate setup super easy!
