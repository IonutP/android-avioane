"""
Interactive Setup Wizard for Android Automation
Helps you set coordinates and OCR regions by tapping and selecting on screen
"""

import time
import json
import os
from pathlib import Path

try:
    import uiautomator2 as u2
    USE_UIAUTOMATOR = True
except ImportError:
    USE_UIAUTOMATOR = False
    print("❌ uiautomator2 not installed. Install it first: pip install uiautomator2")

try:
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np
    IMAGE_AVAILABLE = True
except ImportError:
    IMAGE_AVAILABLE = False
    print("⚠️  PIL not available - install: pip install pillow")


class SetupWizard:
    def __init__(self):
        if USE_UIAUTOMATOR:
            try:
                self.device = u2.connect()
                print("✅ Connected to device")
            except Exception as e:
                print(f"❌ Connection failed: {e}")
                self.device = None
        else:
            self.device = None
        
        self.config_file = Path("automation_config.json")
        self.config = {}
        self.screenshots_dir = Path("screenshots")
        self.screenshots_dir.mkdir(exist_ok=True)
    
    def take_screenshot(self, filename="setup_screenshot.png"):
        """Take screenshot"""
        if not self.device:
            print("❌ Device not connected")
            return None
        
        path = self.screenshots_dir / filename
        try:
            self.device.screenshot(str(path))
            return str(path)
        except Exception as e:
            print(f"❌ Screenshot failed: {e}")
            return None
    
    def wait_for_tap(self, prompt):
        """Wait for user to tap screen and return coordinates"""
        print(f"\n{prompt}")
        print("\nMethod 1: Use coordinate logger (easier)")
        print("   Run this in another Termux window:")
        print("   python3 coordinate_logger.py")
        print("   Then tap the screen and note the coordinates")
        print("\nMethod 2: Manual entry")
        print("   Open the screenshot and find the coordinates")
        
        choice = input("\nEnter coordinates manually? (y/n, default=y): ").strip().lower()
        
        if choice == 'n':
            # Try to use uiautomator2 to monitor touches (advanced)
            print("\n👉 Tap on the screen now...")
            print("   (Monitoring for 5 seconds...)")
            # Note: uiautomator2 doesn't directly capture touch events
            # So we'll use manual entry as fallback
            time.sleep(5)
            print("   (If coordinates weren't detected, use manual entry)")
        
        print("\n📝 Enter the X coordinate: ", end="")
        x = int(input().strip())
        print("📝 Enter the Y coordinate: ", end="")
        y = int(input().strip())
        
        # Test the coordinate
        test = input(f"\n🧪 Test click at ({x}, {y})? (y/n): ").strip().lower()
        if test == 'y':
            self.device.click(x, y)
            time.sleep(1)
            correct = input("   Did it click correctly? (y/n): ").strip().lower()
            if correct != 'y':
                print("   Let's try again...")
                return self.wait_for_tap(prompt)
        
        return (x, y)
    
    def select_region(self, screenshot_path, prompt):
        """Let user select a region by drawing rectangle"""
        print(f"\n{prompt}")
        
        if screenshot_path and os.path.exists(screenshot_path):
            print(f"📸 Screenshot saved: {screenshot_path}")
            print("   Open this image to see where to select the region")
            print("   (You can view it in your phone's gallery)")
        
        print("\nEnter region coordinates:")
        print("  (Top-left corner X, Y, then width and height)")
        x = int(input("  Top-left X coordinate: "))
        y = int(input("  Top-left Y coordinate: "))
        w = int(input("  Width: "))
        h = int(input("  Height: "))
        
        # Show the selected region on screenshot
        if IMAGE_AVAILABLE and screenshot_path and os.path.exists(screenshot_path):
            try:
                img = Image.open(screenshot_path)
                draw = ImageDraw.Draw(img)
                # Draw rectangle with label
                draw.rectangle([x, y, x + w, y + h], outline="red", width=5)
                # Add text label
                try:
                    font = ImageFont.truetype("/system/fonts/Roboto-Regular.ttf", 30)
                except:
                    font = ImageFont.load_default()
                draw.text((x, y - 35), f"Selected Region", fill="red", font=font)
                # Save marked screenshot
                marked_path = screenshot_path.replace(".png", "_marked.png")
                img.save(marked_path)
                print(f"\n✅ Saved marked screenshot: {marked_path}")
                print("   Open it to verify the red rectangle is correct!")
                
                # Ask if correct
                correct = input("\n   Is the region correct? (y/n): ").strip().lower()
                if correct != 'y':
                    print("   Let's try again...")
                    return self.select_region(screenshot_path, prompt)
            except Exception as e:
                print(f"   ⚠️  Could not mark screenshot: {e}")
        
        return (x, y, w, h)
    
    def setup_coordinates(self):
        """Interactive coordinate setup"""
        print("\n" + "="*60)
        print("STEP 1: Setting Up Click Coordinates")
        print("="*60)
        
        # Take initial screenshot
        print("\n📸 Taking screenshot of your game...")
        print("   Make sure Virtual Truck Manager 3 is open and visible!")
        input("   Press Enter when game is ready...")
        time.sleep(1)
        screenshot = self.take_screenshot("game_screenshot.png")
        
        if screenshot:
            print(f"✅ Screenshot saved: {screenshot}")
            print("   📱 Open this image in your gallery to see coordinates")
            print("   💡 Tip: Use an app like 'Touch Coordinates' to see live X,Y as you tap")
            input("   Press Enter to continue...")
        
        # Start click coordinate
        print("\n📍 Setting START CLICK coordinate (car image)")
        x, y = self.wait_for_tap("Where do you click to start? (the car)")
        self.config['start_click'] = {'x': x, 'y': y}
        print(f"✅ Start click set to: ({x}, {y})")
        
        # Button region
        print("\n📍 Setting BUTTON region (upgrade button)")
        print("   This is the area where the upgrade button appears")
        x, y, w, h = self.select_region(screenshot, "Select the button region:")
        self.config['button'] = {'x': x, 'y': y, 'width': w, 'height': h}
        print(f"✅ Button region set: ({x}, {y}) size {w}x{h}")
        
        # Reset clicks
        print("\n📍 Setting RESET CLICK 1 (first reset button)")
        x, y = self.wait_for_tap("Where is the first reset click?")
        self.config['reset_click_1'] = {'x': x, 'y': y}
        
        print("\n📍 Setting RESET CLICK 2 (second reset button)")
        x, y = self.wait_for_tap("Where is the second reset click?")
        self.config['reset_click_2'] = {'x': x, 'y': y}
        
        print("\n📍 Setting RESET CLICK 3 (third reset button)")
        x, y = self.wait_for_tap("Where is the third reset click?")
        self.config['reset_click_3'] = {'x': x, 'y': y}
        
        # Post-timer clicks
        print("\n📍 Setting POST-TIMER CLICK 1")
        x, y = self.wait_for_tap("Where is the first post-timer click?")
        self.config['post_timer_click_1'] = {'x': x, 'y': y}
        
        print("\n📍 Setting POST-TIMER CLICK 2")
        x, y = self.wait_for_tap("Where is the second post-timer click?")
        self.config['post_timer_click_2'] = {'x': x, 'y': y}
    
    def setup_ocr_regions(self):
        """Interactive OCR region setup"""
        print("\n" + "="*60)
        print("STEP 2: Setting Up OCR Regions")
        print("="*60)
        
        screenshot = self.take_screenshot("ocr_setup_screenshot.png")
        
        # OCR above button
        print("\n📝 Setting OCR REGION ABOVE BUTTON")
        print("   This is where step numbers appear (like '10/20', '20/30')")
        x, y, w, h = self.select_region(screenshot, "Select the region above the button:")
        self.config['ocr_above'] = {'x': x, 'y': y, 'width': w, 'height': h}
        
        # OCR second region
        print("\n📝 Setting OCR REGION FOR AMOUNT (step 2/10)")
        print("   This is where the amount appears at step 2/10")
        x, y, w, h = self.select_region(screenshot, "Select the amount region:")
        self.config['ocr_second'] = {'x': x, 'y': y, 'width': w, 'height': h}
        
        # Timer OCR region
        print("\n📝 Setting TIMER OCR REGION")
        print("   This is where the timer appears (like '00:05')")
        x, y, w, h = self.select_region(screenshot, "Select the timer region:")
        self.config['timer_ocr'] = {'x': x, 'y': y, 'width': w, 'height': h}
    
    def setup_thresholds(self):
        """Setup game thresholds"""
        print("\n" + "="*60)
        print("STEP 3: Setting Up Game Thresholds")
        print("="*60)
        
        print("\n⚙️  Reset Target Amount")
        print("   What's the maximum button amount after reset? (usually 10 or 12)")
        amount = int(input("   Enter amount: "))
        self.config['reset_target_amount'] = amount
        
        print("\n⚙️  Timer Threshold (seconds)")
        print("   If timer is above this, reset. (usually 5)")
        threshold = int(input("   Enter threshold: "))
        self.config['timer_threshold'] = threshold
        
        print("\n⚙️  Amount Threshold")
        print("   Minimum amount at step 2/10 to continue (usually 20)")
        amount_threshold = int(input("   Enter threshold: "))
        self.config['amount_threshold'] = amount_threshold
        
        print("\n⚙️  Final Step Target")
        print("   What step means completion? (like '20/30')")
        final_step = input("   Enter target: ").strip()
        self.config['final_step_target'] = final_step
    
    def test_coordinates(self):
        """Test the coordinates"""
        print("\n" + "="*60)
        print("STEP 4: Testing Coordinates")
        print("="*60)
        
        print("\n🧪 Testing coordinates...")
        print("   The script will click each coordinate")
        print("   Watch your game to verify they're correct!")
        
        input("\nPress Enter to start testing...")
        
        # Test start click
        if 'start_click' in self.config:
            print(f"\n📍 Testing start click: {self.config['start_click']}")
            self.device.click(self.config['start_click']['x'], self.config['start_click']['y'])
            time.sleep(1)
            response = input("   Did it click correctly? (y/n): ")
            if response.lower() != 'y':
                print("   Let's fix it...")
                x, y = self.wait_for_tap("Tap the correct location:")
                self.config['start_click'] = {'x': x, 'y': y}
        
        # Test button click
        if 'button' in self.config:
            btn = self.config['button']
            center_x = btn['x'] + btn['width'] // 2
            center_y = btn['y'] + btn['height'] // 2
            print(f"\n📍 Testing button click: ({center_x}, {center_y})")
            self.device.click(center_x, center_y)
            time.sleep(1)
            response = input("   Did it click correctly? (y/n): ")
            if response.lower() != 'y':
                print("   Let's fix the button region...")
                screenshot = self.take_screenshot()
                x, y, w, h = self.select_region(screenshot, "Select correct button region:")
                self.config['button'] = {'x': x, 'y': y, 'width': w, 'height': h}
    
    def save_config(self):
        """Save configuration to file"""
        print("\n" + "="*60)
        print("Saving Configuration")
        print("="*60)
        
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
        
        print(f"✅ Configuration saved to: {self.config_file}")
        print("\n📋 Summary:")
        print(f"   Start click: {self.config.get('start_click', {})}")
        print(f"   Button region: {self.config.get('button', {})}")
        print(f"   Reset clicks: {len([k for k in self.config.keys() if 'reset_click' in k])} clicks")
        print(f"   OCR regions: {len([k for k in self.config.keys() if 'ocr' in k.lower()])} regions")
    
    def run(self):
        """Run the setup wizard"""
        if not self.device:
            print("❌ Cannot connect to device. Make sure uiautomator2 is initialized.")
            return
        
        print("""
╔═══════════════════════════════════════════════════════╗
║     Android Automation - Setup Wizard               ║
╚═══════════════════════════════════════════════════════╝

This wizard will help you set up all coordinates and
OCR regions by tapping and selecting on your screen.

Make sure Virtual Truck Manager 3 is OPEN before starting!
        """)
        
        input("Press Enter to start setup wizard...")
        
        try:
            # Step 1: Coordinates
            self.setup_coordinates()
            
            # Step 2: OCR regions
            self.setup_ocr_regions()
            
            # Step 3: Thresholds
            self.setup_thresholds()
            
            # Step 4: Test
            test = input("\n🧪 Do you want to test the coordinates? (y/n): ")
            if test.lower() == 'y':
                self.test_coordinates()
            
            # Save
            self.save_config()
            
            print("\n" + "="*60)
            print("✅ Setup Complete!")
            print("="*60)
            print(f"\nConfiguration saved to: {self.config_file}")
            print("\nNext steps:")
            print("1. The main script will automatically use this config")
            print("2. Or you can manually copy values to android-automation.py")
            print("3. Run: python3 android-automation.py")
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Setup cancelled by user")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    wizard = SetupWizard()
    wizard.run()
