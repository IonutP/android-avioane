# One Command Setup - Download Everything! 📥

The easiest way to set up - just download everything from a URL!

## Quick Setup (3 Steps)

### Step 1: Install Termux
- Download from [F-Droid](https://f-droid.org/packages/com.termux/)
- Open Termux

### Step 2: Grant Storage Permission
```bash
termux-setup-storage
```
Tap "Allow"

### Step 3: Download and Run!
```bash
cd ~/storage/downloads
wget https://your-url.com/download_and_setup.sh
bash download_and_setup.sh https://your-url.com
bash run.sh
```

**That's it!** Everything downloads and sets up automatically! 🎉

## Hosting Your Files

You need to host the files somewhere accessible. Options:

### Option 1: GitHub (Free & Easy)

1. **Create a GitHub repository**
2. **Upload all files** to the repo
3. **Get the raw file URL:**
   - Go to your file on GitHub
   - Click "Raw" button
   - Copy the URL (remove filename)
   - Example: `https://raw.githubusercontent.com/yourusername/repo/main`

4. **Use it:**
   ```bash
   bash download_and_setup.sh https://raw.githubusercontent.com/yourusername/repo/main
   ```

### Option 2: Your Own Server

If you have a web server:
```bash
bash download_and_setup.sh https://yourserver.com/files
```

### Option 3: Google Drive (via Direct Link)

1. Upload files to Google Drive
2. Get shareable links
3. Convert to direct download links
4. Use in script

## Files Needed on Server

Make sure these files are accessible:
- `android-automation.py`
- `setup_wizard.py`
- `load_config.py`
- `run.sh`
- `launcher.sh`
- `quick_start.sh`
- `download_and_setup.sh` (optional)

## Complete One-Liner

If you host `download_and_setup.sh` online, you can do everything in one command:

```bash
cd ~/storage/downloads && termux-setup-storage && wget -O download_and_setup.sh https://your-url.com/download_and_setup.sh && bash download_and_setup.sh https://your-url.com && bash run.sh
```

## Example: Using GitHub

```bash
# Step 1: Setup storage
termux-setup-storage

# Step 2: Download setup script
cd ~/storage/downloads
wget https://raw.githubusercontent.com/yourusername/repo/main/download_and_setup.sh

# Step 3: Download all files and setup
bash download_and_setup.sh https://raw.githubusercontent.com/yourusername/repo/main

# Step 4: Run automation
bash run.sh
```

## Benefits

- ✅ **No manual file copying** - Everything downloads automatically
- ✅ **Easy updates** - Just update files on server, re-download
- ✅ **Works on any device** - Just need the URL
- ✅ **Share with others** - Give them the URL, they're done!

## Security Note

Only download from trusted sources! Make sure the URL is yours or from a trusted repository.
