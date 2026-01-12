# GitHub Repository Setup 🚀

## Create GitHub Repository

1. **Go to GitHub** and create a new repository:
   - Name: `android-avioane` (or your preferred name)
   - Visibility: Public or Private
   - **Don't** initialize with README (we already have one)

2. **Copy the repository URL** (you'll need it below)

## Push to GitHub

### Option 1: Using HTTPS

```bash
cd ~/Desktop/android-avioane

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/android-avioane.git

# Commit all files
git add .
git commit -m "Initial commit: Android automation for Virtual Truck Manager 3"

# Push to GitHub
git branch -M main
git push -u origin main
```

### Option 2: Using SSH

```bash
cd ~/Desktop/android-avioane

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin git@github.com:YOUR_USERNAME/android-avioane.git

# Commit all files
git add .
git commit -m "Initial commit: Android automation for Virtual Truck Manager 3"

# Push to GitHub
git branch -M main
git push -u origin main
```

## Update Download URLs

After pushing to GitHub, update the download URLs in:

1. **`download_and_setup.sh`** - Change the default URL:
   ```bash
   DEFAULT_URL="https://raw.githubusercontent.com/YOUR_USERNAME/android-avioane/main"
   ```

2. **`ULTIMATE_QUICK_START.md`** - Update example URLs

3. **`README_DOWNLOAD.md`** - Update example URLs

4. **`README.md`** - Update quick start URLs

## Get Raw File URLs

For any file in your GitHub repo:
1. Go to the file on GitHub
2. Click the **"Raw"** button
3. Copy the URL
4. Remove the filename to get the base URL

Example:
- File: `https://github.com/yourusername/android-avioane/blob/main/run.sh`
- Raw: `https://raw.githubusercontent.com/yourusername/android-avioane/main/run.sh`
- Base: `https://raw.githubusercontent.com/yourusername/android-avioane/main`

## Test Download

Test that files are accessible:

```bash
# Test download
wget https://raw.githubusercontent.com/YOUR_USERNAME/android-avioane/main/run.sh

# Should download successfully
```

## Future Updates

To update files on GitHub:

```bash
cd ~/Desktop/android-avioane
git add .
git commit -m "Update: [describe changes]"
git push
```

## Share with Others

Once set up, share this command with others:

```bash
termux-setup-storage && cd ~/storage/downloads && pkg install -y wget && wget -O download_and_setup.sh https://raw.githubusercontent.com/YOUR_USERNAME/android-avioane/main/download_and_setup.sh && bash download_and_setup.sh https://raw.githubusercontent.com/YOUR_USERNAME/android-avioane/main && bash run.sh
```

Replace `YOUR_USERNAME` with your actual GitHub username!
