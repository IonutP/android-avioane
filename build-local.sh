#!/bin/bash
# Local build script using existing Android SDK

echo "🔨 Building APK locally..."
echo ""

# Check for Android SDK
if [ -n "$ANDROID_HOME" ]; then
    ANDROID_SDK="$ANDROID_HOME"
elif [ -n "$ANDROID_SDK_ROOT" ]; then
    ANDROID_SDK="$ANDROID_SDK_ROOT"
elif [ -d "$HOME/Library/Android/sdk" ]; then
    ANDROID_SDK="$HOME/Library/Android/sdk"
elif [ -d "$HOME/Android/Sdk" ]; then
    ANDROID_SDK="$HOME/Android/Sdk"
else
    echo "❌ Android SDK not found!"
    echo ""
    echo "Please set ANDROID_HOME or ANDROID_SDK_ROOT environment variable"
    echo "Or install Android SDK and set:"
    echo "  export ANDROID_HOME=\$HOME/Library/Android/sdk"
    echo "  export PATH=\$PATH:\$ANDROID_HOME/tools:\$ANDROID_HOME/platform-tools"
    exit 1
fi

echo "✅ Found Android SDK at: $ANDROID_SDK"
echo ""

# Check for buildozer
if ! command -v buildozer &> /dev/null; then
    echo "📦 Installing buildozer..."
    pip3 install buildozer cython
fi

# Accept licenses if needed
if [ -d "$ANDROID_SDK/licenses" ]; then
    echo "📝 Accepting Android SDK licenses..."
    mkdir -p "$ANDROID_SDK/licenses"
    echo "24333bdce4ebe0d787f322fb67ed0efb197b3185" > "$ANDROID_SDK/licenses/android-sdk-license"
    echo "601085b94cd77f0b54ff86406957099ebe79c4d6" > "$ANDROID_SDK/licenses/android-sdk-preview-license"
    echo "84831b9409646a918e30573bab4c9c91346d8abd" > "$ANDROID_SDK/licenses/android-sdk-arm-dbt-license"
    echo "d975f751698a77b662f1254ddbeed3901e976f5a" > "$ANDROID_SDK/licenses/intel-android-extra-license"
    echo "33b6a2b64607f11b759f320ef9dff4ae5c47d5a2" > "$ANDROID_SDK/licenses/google-gdk-license"
fi

# Set environment variables for buildozer
export ANDROID_SDK_ROOT="$ANDROID_SDK"
export ANDROID_HOME="$ANDROID_SDK"
export PATH="$PATH:$ANDROID_SDK/tools:$ANDROID_SDK/platform-tools"

# Check for required Android SDK components
echo "🔍 Checking Android SDK components..."
if [ ! -d "$ANDROID_SDK/build-tools" ]; then
    echo "⚠️  Build tools not found. Install via Android Studio SDK Manager"
    echo "   Or run: sdkmanager 'build-tools;33.0.0'"
fi

if [ ! -d "$ANDROID_SDK/platforms" ]; then
    echo "⚠️  Android platforms not found. Install via Android Studio SDK Manager"
    echo "   Or run: sdkmanager 'platforms;android-33'"
fi

# Build
echo ""
echo "🚀 Starting build..."
echo "   This may take 10-30 minutes..."
echo ""

buildozer android debug

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Build successful!"
    echo "📱 APK location: bin/"
    ls -lh bin/*.apk 2>/dev/null || echo "   (check bin/ directory)"
else
    echo ""
    echo "❌ Build failed"
    exit 1
fi
