# Android Avioane Automation 🤖

Automated clicking script for Virtual Truck Manager 3 running directly on Android devices using Termux.

## 🚀 Quick Start

### Option 1: Download Everything (Recommended)

```bash
# 1. Install Termux from F-Droid
# 2. Run:
termux-setup-storage
cd ~/storage/downloads
pkg install -y wget
wget -O download_and_setup.sh https://raw.githubusercontent.com/IonutP/android-avioane/main/download_and_setup.sh
bash download_and_setup.sh https://raw.githubusercontent.com/IonutP/android-avioane/main
bash run.sh
```

### Option 2: Manual Setup

1. **Install Termux** from [F-Droid](https://f-droid.org/packages/com.termux/)
2. **Grant storage permission:**
   ```bash
   termux-setup-storage
   ```
3. **Copy all files** to `~/storage/downloads`
4. **Run:**
   ```bash
   cd ~/storage/downloads
   bash run.sh
   ```

## 📁 Project Structure

```
android-avioane/
├── android-automation.py    # Main automation script
├── setup_wizard.py          # Interactive configuration wizard
├── load_config.py           # Configuration loader
├── run.sh                   # Smart launcher (setup + daily use)
├── download_and_setup.sh    # Download all files from URL
├── quick_start.sh           # One-time setup script
├── launcher.sh              # Daily launcher
├── init_uiautomator2.py     # uiautomator2 initialization helper
├── test_game_package.py     # Find game package name
├── coordinate_logger.py     # Coordinate logging helper
└── *.md                     # Documentation files
```

## 📚 Documentation

- **`ULTIMATE_QUICK_START.md`** - One-command setup guide
- **`SIMPLE_START.md`** - Simple step-by-step guide
- **`START_HERE.md`** - Getting started overview
- **`SETUP_WIZARD_GUIDE.md`** - How to use the setup wizard
- **`TERMUX_SETUP.md`** - Detailed Termux setup instructions
- **`COMPLETE_SETUP_GUIDE.md`** - Complete setup for new devices

## 🎯 Features

- ✅ **Standalone Android automation** - No computer needed
- ✅ **Smart setup** - Automatically installs dependencies
- ✅ **Interactive wizard** - Visual coordinate configuration
- ✅ **OCR-based detection** - Recognizes game state automatically
- ✅ **Timer detection** - Waits for timers to complete
- ✅ **Auto-reset** - Resets game when needed
- ✅ **One-command setup** - Download everything from URL

## 🔧 Requirements

- Android device (root not required)
- Termux app
- Virtual Truck Manager 3 game installed

## 📦 Dependencies

The script automatically installs:
- Python 3
- uiautomator2
- Pillow (PIL)
- NumPy
- pytesseract or easyocr

## 🎮 Usage

### First Time Setup

```bash
bash run.sh
```

This will:
1. Check/install Python
2. Check/install packages
3. Run setup wizard (if config missing)
4. Start automation

### Daily Usage

```bash
cd ~/storage/downloads && bash run.sh
```

Or create an alias:
```bash
echo 'alias autom8="cd ~/storage/downloads && bash run.sh"' >> ~/.bashrc
source ~/.bashrc
autom8
```

## ⚙️ Configuration

Configuration is stored in `automation_config.json` and can be created using:

```bash
python3 setup_wizard.py
```

## 🔄 Updates

To update files from GitHub:

```bash
cd ~/storage/downloads/automation
bash download_and_setup.sh https://raw.githubusercontent.com/IonutP/android-avioane/main
```

## 📝 License

[Add your license here]

## 🤝 Contributing

[Add contribution guidelines here]

## ⚠️ Disclaimer

This is for educational purposes. Use responsibly and in accordance with the game's terms of service.
