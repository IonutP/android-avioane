# 🚀 Super Simple Start - Just One Command!

## For Brand New Device

### Step 1: Install Termux
- Download from [F-Droid](https://f-droid.org/packages/com.termux/)
- Open Termux

### Step 2: Grant Storage Permission
```bash
termux-setup-storage
```
Tap "Allow"

### Step 3: Copy Files
Copy all files to your phone's **Downloads** folder

### Step 4: Run Everything!
```bash
cd ~/storage/downloads
bash run.sh
```

**That's it!** The script will:
- ✅ Check if Python is installed (install if needed)
- ✅ Check if packages are installed (install if needed)
- ✅ Check if configuration exists (run wizard if needed)
- ✅ Run automation when ready

## Daily Usage

Just run:
```bash
cd ~/storage/downloads && bash run.sh
```

One command does everything! 🎉

## What `run.sh` Does

1. **Checks Python** → Installs if missing
2. **Checks packages** → Installs if missing (takes 10-20 min first time)
3. **Checks config** → Runs setup wizard if needed
4. **Runs automation** → Starts clicking!

## Make It Even Easier

Create an alias in Termux:
```bash
echo 'alias autom8="cd ~/storage/downloads && bash run.sh"' >> ~/.bashrc
source ~/.bashrc
```

Then just type: `autom8` 🚀
