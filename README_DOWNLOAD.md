# Download Setup - Host Your Files Online 📥

## Quick Start

### If files are hosted online:

```bash
# 1. Setup storage
termux-setup-storage

# 2. Download setup script
cd ~/storage/downloads
wget https://your-url.com/download_and_setup.sh

# 3. Download all files
bash download_and_setup.sh https://your-url.com

# 4. Run automation
bash run.sh
```

## Hosting Options

### GitHub (Recommended - Free)

1. **Create GitHub repo** (public or private)
2. **Upload all files**
3. **Get raw URL:**
   - Go to: `https://github.com/yourusername/repo`
   - Click a file → "Raw" button
   - URL format: `https://raw.githubusercontent.com/yourusername/repo/main`

4. **Use it:**
   ```bash
   bash download_and_setup.sh https://raw.githubusercontent.com/yourusername/repo/main
   ```

### Your Own Server

If you have web hosting:
```bash
bash download_and_setup.sh https://yourserver.com/path/to/files
```

### Google Drive (via Direct Link)

1. Upload files
2. Get shareable links
3. Convert to direct download
4. Use in script

## Files to Host

Upload these files to your server/repo:
- ✅ `android-automation.py`
- ✅ `setup_wizard.py`
- ✅ `load_config.py`
- ✅ `run.sh`
- ✅ `launcher.sh`
- ✅ `quick_start.sh`
- ✅ `download_and_setup.sh` (optional)

## Complete Workflow

**First time on new device:**
```bash
# Install Termux, then:
termux-setup-storage
cd ~/storage/downloads
wget https://your-url.com/download_and_setup.sh
bash download_and_setup.sh https://your-url.com
bash run.sh
```

**Daily usage:**
```bash
cd ~/storage/downloads/automation && bash run.sh
```

## Update Files

To update files:
```bash
cd ~/storage/downloads/automation
bash download_and_setup.sh https://your-url.com
```

All files will be re-downloaded and updated!
