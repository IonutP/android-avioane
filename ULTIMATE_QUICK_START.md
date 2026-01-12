# 🚀 Ultimate Quick Start - One Command Does Everything!

## For Brand New Device (3 Steps)

### Step 1: Install Termux
Download from [F-Droid](https://f-droid.org/packages/com.termux/)

**Note:** Termux home directory is `/data/data/com.termux/files/home`
After running `termux-setup-storage`, `~/storage/downloads` links to your Downloads folder.

### Step 2: Run This One Command
```bash
termux-setup-storage && cd ~/storage/downloads && pkg install -y wget && wget -O download_and_setup.sh https://your-url.com/download_and_setup.sh && bash download_and_setup.sh https://your-url.com && bash run.sh
```

**Replace `https://your-url.com` with your actual file URL!**

### Step 3: Done! 🎉

The script will:
- ✅ Grant storage permission
- ✅ Install wget
- ✅ Download all files
- ✅ Install Python and packages
- ✅ Run setup wizard (if needed)
- ✅ Start automation

## What You Need

**Just host your files online:**
- GitHub (free, recommended)
- Your own server
- Any file hosting service

## GitHub Example

If you host on GitHub at `https://github.com/yourusername/repo`:

```bash
termux-setup-storage && cd ~/storage/downloads && pkg install -y wget && wget -O download_and_setup.sh https://raw.githubusercontent.com/yourusername/repo/main/download_and_setup.sh && bash download_and_setup.sh https://raw.githubusercontent.com/yourusername/repo/main && bash run.sh
```

## Daily Usage (After First Setup)

```bash
cd ~/storage/downloads/automation && bash run.sh
```

Or create alias:
```bash
echo 'alias autom8="cd ~/storage/downloads/automation && bash run.sh"' >> ~/.bashrc
source ~/.bashrc
```

Then just: `autom8` 🚀

## Files to Host Online

Upload these to your GitHub/server:
- `android-automation.py`
- `setup_wizard.py`
- `load_config.py`
- `run.sh`
- `launcher.sh`
- `quick_start.sh`
- `download_and_setup.sh`

## That's It!

One command downloads everything and sets it up automatically! 🎉
