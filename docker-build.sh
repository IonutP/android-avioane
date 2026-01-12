#!/bin/bash
# Build APK using Docker

echo "🐳 Building Android APK using Docker..."
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running or not accessible"
    echo ""
    echo "Please:"
    echo "1. Make sure Docker Desktop is running"
    echo "2. On macOS: Open Docker Desktop app"
    echo "3. Wait for Docker to start (whale icon in menu bar)"
    echo "4. Try again"
    exit 1
fi

# Build Docker image
echo "📦 Building Docker image..."
docker build -t android-avioane-builder .

if [ $? -ne 0 ]; then
    echo "❌ Docker build failed"
    exit 1
fi

echo ""
echo "✅ Docker image built successfully"
echo ""
echo "🔨 Building APK (this will take 30-60 minutes first time)..."
echo ""

# Run buildozer in container
docker run --rm -it \
    -v "$(pwd):/app" \
    -v "$HOME/.buildozer:/root/.buildozer" \
    android-avioane-builder \
    buildozer android debug

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ APK built successfully!"
    echo "📱 Find your APK in: bin/"
    ls -lh bin/*.apk 2>/dev/null || echo "   (check bin/ directory)"
else
    echo ""
    echo "❌ Build failed"
    exit 1
fi
