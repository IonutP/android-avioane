# How to Run the Automation Script While in Game

## Method 1: Automatic App Switching (Easiest) ⭐ Recommended

1. **Find your game's package name:**
   - Open your game
   - Connect your device to a computer with ADB
   - Run: `adb shell dumpsys window | grep mCurrentFocus`
   - Look for something like: `com.example.gamename`
   - Or use an app like "Package Name Viewer" from Play Store

2. **Set the package name in the script:**
   - Open `android-automation.py` in Pydroid 3
   - Find this line near the bottom:
     ```python
     GAME_PACKAGE = None  # <-- SET THIS TO YOUR GAME PACKAGE NAME
     ```
   - Change it to:
     ```python
     GAME_PACKAGE = "com.your.game.package"  # Replace with your game's package
     ```

3. **Run the script:**
   - Tap the **Run** button (▶️) in Pydroid 3
   - The script will automatically switch to your game
   - Automation will start immediately

## Method 2: Manual Switching (If you don't know package name)

1. **Open your game first** - Make sure the game is running

2. **Open Pydroid 3** (use split-screen or recent apps)

3. **Run the script:**
   - Tap the **Run** button (▶️) in Pydroid 3
   - You'll see: "Waiting 5 seconds for you to switch to the game..."
   - **Quickly switch back to your game** (use recent apps button)
   - The script will start after 5 seconds

## Method 3: Split Screen (Best for Monitoring)

1. **Enable Split Screen:**
   - Open your game
   - Open recent apps (square button)
   - Long-press on Pydroid 3
   - Select "Split screen"
   - Position Pydroid 3 on top or bottom

2. **Run the script:**
   - Tap **Run** in Pydroid 3
   - You can see the script output while the game runs
   - The game will be in the other half of the screen

## Method 4: Floating Window (Pydroid 3 Pro)

If you have Pydroid 3 Pro:

1. **Enable floating window** for Pydroid 3
2. **Run the script**
3. **Minimize Pydroid 3** to a small floating window
4. The game will be full screen, script runs in background

## Tips for Best Results

### Keep Screen On
- Go to **Settings** → **Display** → **Screen timeout**
- Set to **30 minutes** or **Never** (while charging)
- Or use an app like "Stay Awake" to keep screen on

### Disable Battery Optimization
- Go to **Settings** → **Battery** → **Battery optimization**
- Find **Pydroid 3** and set to **Don't optimize**
- This prevents the script from being killed

### Use ADB Over WiFi (Optional)
If you want to run without USB:
1. Enable **Wireless debugging** in Developer Options
2. Note the IP and port (e.g., `192.168.1.100:5555`)
3. Connect from computer: `adb connect 192.168.1.100:5555`
4. Now the script can run even without USB

### Test First
Before running the full automation:
1. Test that clicking works
2. Verify coordinates are correct for your screen
3. Make sure OCR can read the text

## Troubleshooting

### Script stops when you switch apps
- Make sure ADB is connected
- Check that the script is still running in Pydroid 3
- Try Method 1 (automatic switching) instead

### Clicks don't work
- Make sure the game is in the foreground
- Verify coordinates are correct for your screen size
- Check that ADB has proper permissions

### Script runs but game doesn't respond
- The game might be blocking automation
- Try running the script with the game already open
- Some games detect automation - this is normal

### Pydroid 3 closes when you switch apps
- Disable battery optimization for Pydroid 3
- Keep Pydroid 3 in recent apps
- Use split-screen mode

## Quick Start Checklist

- [ ] Game is installed and can be opened
- [ ] USB Debugging is enabled
- [ ] ADB connection works (`adb devices` shows your device)
- [ ] Python packages are installed in Pydroid 3
- [ ] Coordinates are set correctly in the script
- [ ] Screen timeout is set to long/never
- [ ] Battery optimization is disabled for Pydroid 3

## Example Workflow

1. **Prepare:**
   - Open your game
   - Note the package name (or leave as None)
   - Set coordinates in script

2. **Run:**
   - Open Pydroid 3
   - Run `android-automation.py`
   - If using Method 2, quickly switch to game

3. **Monitor:**
   - Check Pydroid 3 output for status
   - Watch the game to verify it's working
   - Let it run!

4. **Stop:**
   - Go back to Pydroid 3
   - Press **Stop** button or Ctrl+C
   - Automation will stop gracefully
