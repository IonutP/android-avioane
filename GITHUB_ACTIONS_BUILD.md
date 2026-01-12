# Build APK with GitHub Actions 🚀

Easiest way to build the APK - no Docker needed on your machine!

## How It Works

GitHub Actions will automatically build the APK whenever you:
- Push code to the `main` branch
- Create a pull request
- Manually trigger it (workflow_dispatch)

## Setup (Already Done!)

The workflow file (`.github/workflows/build-apk.yml`) is already created and committed.

## Build the APK

### Option 1: Push to GitHub (Automatic)

Just push your code:
```bash
git push origin main
```

GitHub Actions will automatically build the APK!

### Option 2: Manual Trigger

1. Go to your GitHub repository: https://github.com/IonutP/android-avioane
2. Click on **"Actions"** tab
3. Select **"Build Android APK"** workflow
4. Click **"Run workflow"** button
5. Click **"Run workflow"** again

The build will start automatically!

## Get Your APK

After the build completes:

1. Go to **Actions** tab in GitHub
2. Click on the latest workflow run
3. Scroll down to **"Artifacts"** section
4. Download **"gameautomation-apk"**
5. Extract the ZIP file to get your APK!

## Build Time

- **First build**: 30-60 minutes (downloads Android SDK)
- **Subsequent builds**: 10-20 minutes (uses cache)

## What Gets Built

The workflow will:
1. ✅ Checkout your code
2. ✅ Install all dependencies
3. ✅ Build the APK using buildozer
4. ✅ Upload APK as an artifact
5. ✅ Make it available for download

## Install the APK

1. Download the APK from GitHub Actions artifacts
2. Transfer to your device or drag into BlueStacks
3. Install the APK
4. Grant overlay permission
5. Open your game and use the overlay!

## Advantages

- ✅ No Docker needed on your machine
- ✅ No local build setup required
- ✅ Automatic builds on every push
- ✅ APK stored in GitHub for easy access
- ✅ Works on any computer (just push code)

## Troubleshooting

### Build fails
- Check the Actions tab for error messages
- Make sure all required files are committed
- Check that `buildozer.spec` is correct

### Can't find APK
- Go to Actions tab
- Click on the workflow run
- Scroll to Artifacts section
- Download the artifact ZIP

### Want to trigger manually?
- Go to Actions → Build Android APK → Run workflow

## Next Steps

1. **Push your code** (or manually trigger the workflow)
2. **Wait for build** (30-60 min first time)
3. **Download APK** from Actions artifacts
4. **Install and test** in BlueStacks or on device!

No Docker needed - GitHub does all the work! 🎉
