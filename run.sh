#!/bin/bash
# Smart Launcher - Does everything automatically!
# Run this script and it will:
# - Check if setup is needed
# - Run setup if needed
# - Run automation if ready
# Just run: bash run.sh (or make it executable and run: ./run.sh)

clear
echo "╔═══════════════════════════════════════════════════════╗"
echo "║     Virtual Truck Manager 3 - Smart Launcher         ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Python is installed
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${YELLOW}⚠️  Python not found - installing...${NC}"
        pkg install -y python python-pip
        if [ $? -ne 0 ]; then
            echo -e "${RED}❌ Failed to install Python${NC}"
            return 1
        fi
    fi
    return 0
}

# Check if packages are installed
check_packages() {
    echo "🔍 Checking Python packages..."
    
    python3 -c "import uiautomator2" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo -e "${YELLOW}⚠️  Missing packages - installing...${NC}"
        echo "   This may take 10-20 minutes..."
        # Ensure python-pip is installed (Termux requirement)
        pkg install -y python-pip 2>/dev/null || true
        
        # Try Termux packages first (pre-built, no compilation needed)
        echo "   Installing pillow from Termux packages (recommended - avoids build errors)..."
        if pkg install -y python-pillow 2>/dev/null; then
            echo "   ✅ Pillow installed from Termux package"
        else
            echo -e "${YELLOW}   ⚠️  Termux pillow package not available, trying pip with JPEG support...${NC}"
            # Install JPEG development libraries (required for Pillow compilation)
            echo "   Installing JPEG development libraries..."
            pkg install -y libjpeg-turbo-dev 2>/dev/null || pkg install -y libjpeg-turbo 2>/dev/null || true
            pkg install -y binutils make gcc python-dev zlib libpng 2>/dev/null || true
            # Set environment variables for JPEG library location
            export JPEG_ROOT=/data/data/com.termux/files/usr
            export CPPFLAGS="-I$JPEG_ROOT/include"
            export LDFLAGS="-L$JPEG_ROOT/lib"
            python3 -m pip install --user pillow || echo "   ⚠️  Pillow installation failed, but continuing..."
        fi
        
        echo "   Installing numpy from Termux packages (recommended)..."
        pkg install -y python-numpy 2>/dev/null || {
            echo -e "${YELLOW}   ⚠️  Termux numpy package not available, trying pip...${NC}"
            # Install build dependencies if we need to build from source
            pkg install -y binutils make gcc python-dev 2>/dev/null || true
            python3 -m pip install --user numpy || echo "   ⚠️  NumPy installation failed, but continuing..."
        }
        
        echo "   Installing pytesseract..."
        python3 -m pip install --user pytesseract || echo "   ⚠️  pytesseract installation had issues, continuing..."
        
        echo "   Installing uiautomator2..."
        # Install libxml2 and libxslt dev packages (required for lxml, which uiautomator2 needs)
        pkg install -y libxml2-dev libxslt-dev 2>/dev/null || pkg install -y libxml2 libxslt 2>/dev/null || true
        python3 -m pip install --user uiautomator2 || {
            echo -e "${RED}   ❌ uiautomator2 installation failed${NC}"
            echo -e "${YELLOW}   Try installing libxml2 and libxslt dev packages manually:${NC}"
            echo -e "${YELLOW}   pkg install -y libxml2-dev libxslt-dev${NC}"
            return 1
        }
        
        if [ $? -ne 0 ]; then
            echo -e "${RED}❌ Package installation failed${NC}"
            return 1
        fi
        
        echo -e "${GREEN}✅ Packages installed${NC}"
        echo ""
        echo "🔧 Installing ADB (required for uiautomator2)..."
        pkg install -y android-tools 2>/dev/null || {
            echo -e "${YELLOW}   ⚠️  android-tools installation failed, but continuing...${NC}"
        }
        echo ""
        echo "🔧 Initializing uiautomator2 (one time)..."
        echo "   ⚠️  Grant permissions when prompted!"
        python3 -m uiautomator2 init
        
        if [ $? -ne 0 ]; then
            echo -e "${YELLOW}⚠️  uiautomator2 init had issues, but continuing...${NC}"
        fi
    fi
    
    return 0
}

# Check if config exists
check_config() {
    if [ ! -f "automation_config.json" ]; then
        echo -e "${YELLOW}⚠️  Configuration not found${NC}"
        echo ""
        echo "Running setup wizard..."
        echo "   This will help you configure coordinates and OCR regions"
        echo ""
        read -p "Press Enter to start setup wizard..."
        
        python3 setup_wizard.py
        
        if [ ! -f "automation_config.json" ]; then
            echo -e "${RED}❌ Setup wizard did not create config file${NC}"
            echo "   Please run setup wizard manually: python3 setup_wizard.py"
            return 1
        fi
        
        echo -e "${GREEN}✅ Configuration created!${NC}"
        echo ""
    fi
    
    return 0
}

# Main execution
main() {
    echo "🔍 Checking requirements..."
    echo ""
    
    # Step 1: Check Python
    if ! check_python; then
        echo -e "${RED}❌ Setup failed. Please install Python manually.${NC}"
        exit 1
    fi
    echo -e "${GREEN}✅ Python installed${NC}"
    
    # Step 2: Check packages
    if ! check_packages; then
        echo -e "${RED}❌ Package installation failed${NC}"
        exit 1
    fi
    echo -e "${GREEN}✅ Packages ready${NC}"
    
    # Step 3: Check config
    if ! check_config; then
        echo -e "${RED}❌ Configuration setup failed${NC}"
        exit 1
    fi
    echo -e "${GREEN}✅ Configuration ready${NC}"
    
    echo ""
    echo "═══════════════════════════════════════════════════════"
    echo -e "${GREEN}✅ Everything is ready!${NC}"
    echo "═══════════════════════════════════════════════════════"
    echo ""
    echo "Starting automation in 3 seconds..."
    echo "Make sure Virtual Truck Manager 3 is ready!"
    echo ""
    
    sleep 3
    
    # Run the automation
    python3 android-automation.py
}

# Run main function
main
