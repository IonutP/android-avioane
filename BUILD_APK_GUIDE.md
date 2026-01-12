# Build Android APK - Simple Guide 📱

This guide will help you build a simple Android app with a GUI for setting coordinates and running automation.

## Prerequisites

- **Linux** (or WSL on Windows, or macOS)
- **Python 3.8+**
- **Android SDK** (will be installed automatically by Buildozer)

## Quick Start

### Step 1: Install Buildozer

```bash
pip install buildozer
```

### Step 2: Install Dependencies (Linux)

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y git zip unzip openjdk-11-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Fedora
sudo dnf install -y git zip unzip java-11-openjdk-devel python3-pip autoconf libtool pkg-config zlib-devel ncurses-devel cmake libffi-devel openssl-devel
```

### Step 3: Initialize Buildozer

```bash
cd /path/to/android-avioane
buildozer init
```

This creates a `buildozer.spec` file (already created for you).

### Step 4: Build APK

```bash
buildozer android debug
```

This will:
- Download Android SDK and NDK (first time only, ~1GB)
- Compile Python and all dependencies
- Build the APK
- Takes 30-60 minutes first time, 5-10 minutes after

### Step 5: Get Your APK

After building, find your APK in:
```
bin/gameautomation-0.1-arm64-v8a-debug.apk
```

### Step 6: Install on Device/BlueStacks

1. Transfer APK to your device or BlueStacks
2. Enable "Install from Unknown Sources" in settings
3. Tap the APK to install
4. Open the app!

## What the App Does

The app provides a simple GUI where you can:

1. **Set Click Coordinates**
   - Enter X, Y coordinates for each click point
   - Start click, reset clicks, etc.

2. **Set OCR Regions**
   - Enter X, Y, Width, Height for OCR areas
   - OCR above button, timer region, etc.

3. **Set Thresholds**
   - Reset target amount
   - Timer threshold
   - Amount threshold
   - Final step target

4. **Save/Load Config**
   - Save your configuration
   - Load saved configurations

5. **Test & Run**
   - Test coordinates
   - Run automation

## Testing in BlueStacks

1. **Install BlueStacks** on your computer
2. **Enable Developer Options** in BlueStacks:
   - Settings → About → Tap "Build number" 7 times
3. **Enable USB Debugging** in BlueStacks
4. **Install APK**:
   - Drag APK into BlueStacks, or
   - Use ADB: `adb install gameautomation-0.1-arm64-v8a-debug.apk`
5. **Run the app** in BlueStacks

## Troubleshooting

### "buildozer: command not found"
```bash
pip install --user buildozer
export PATH=$PATH:~/.local/bin
```

### Build fails with "No module named 'Cython'"
```bash
pip install cython
```

### Build fails with Java errors
Make sure Java 11 is installed:
```bash
sudo apt install openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

### APK is too large
Edit `buildozer.spec` and remove unused requirements.

### Want to test on real device first?
Just install the APK directly on your Android phone via USB or file transfer.

## Next Steps

Once you have the APK working:

1. **Test in BlueStacks** - Make sure coordinates work
2. **Adjust coordinates** - Use the GUI to fine-tune
3. **Test OCR regions** - Make sure OCR can read text
4. **Run automation** - Start the automation and monitor

## Alternative: Use Existing Apps

If building is too complex, consider:

- **MacroDroid** - GUI-based automation, no coding
- **Tasker + AutoInput** - Very powerful, GUI-based
- **Automate** - Free alternative to MacroDroid

These apps can do everything the automation does, with a GUI interface!
