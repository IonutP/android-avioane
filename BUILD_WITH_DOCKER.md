# Build APK with Docker 🐳

Easiest way to build the Android APK on macOS or any system!

## Prerequisites

- **Docker Desktop** installed ([Download here](https://www.docker.com/products/docker-desktop/))

## Quick Build

### Step 1: Make script executable

```bash
chmod +x docker-build.sh
```

### Step 2: Run the build

```bash
./docker-build.sh
```

That's it! The script will:
1. Build a Docker image with all dependencies
2. Run buildozer inside Docker
3. Output the APK to `bin/` folder

## What Happens

1. **First time**: Downloads Android SDK/NDK (~1GB, takes 30-60 minutes)
2. **Subsequent builds**: Much faster (5-10 minutes)
3. **Output**: APK file in `bin/` directory

## Manual Docker Build

If you prefer to run commands manually:

```bash
# Build Docker image
docker build -t android-avioane-builder .

# Run buildozer
docker run --rm -it \
    -v "$(pwd):/app" \
    -v "$HOME/.buildozer:/root/.buildozer" \
    android-avioane-builder \
    buildozer android debug
```

## Get Your APK

After building, find your APK:
```bash
ls -lh bin/*.apk
```

The APK will be named something like:
```
bin/gameautomation-0.1-arm64-v8a-debug.apk
```

## Install on BlueStacks/Device

1. **Transfer APK** to your device or drag into BlueStacks
2. **Install** the APK
3. **Grant overlay permission** when prompted
4. **Open your game** and use the overlay!

## Troubleshooting

### Docker not found
Install Docker Desktop from https://www.docker.com/products/docker-desktop/

### Build fails
Check the error output. Common issues:
- Network issues (Docker needs internet)
- Disk space (need ~5GB free)
- Memory (Docker needs at least 4GB RAM allocated)

### Want to see build progress?
The build shows progress. First build downloads Android SDK which takes time.

### Build takes too long?
First build is always slow (downloads Android SDK). Subsequent builds are much faster.

## Alternative: GitHub Actions

If you don't want to build locally, you can use GitHub Actions to build automatically. I can set that up if you want!
