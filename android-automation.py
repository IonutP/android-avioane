"""
Android Game Automation Script for Pydroid 3
Automates clicking and upgrading in a game directly on Android device

Requirements (install via Pydroid 3 pip):
- uiautomator2 (for UI automation) OR use adb commands
- pillow (PIL) - for image processing (FREE)
- numpy - for image processing (FREE)
- pytesseract OR easyocr - for OCR text recognition

Note: opencv-python is NOT required - using PIL/Pillow instead (free alternative)

Alternative: If uiautomator2 doesn't work, we can use adb commands via subprocess
"""

import time
import os
import subprocess
from pathlib import Path

try:
    import uiautomator2 as u2
    USE_UIAUTOMATOR = True
except ImportError:
    USE_UIAUTOMATOR = False
    print("⚠️  uiautomator2 not available, will use ADB commands")

try:
    from PIL import Image, ImageOps, ImageEnhance
    import numpy as np
    IMAGE_PROCESSING_AVAILABLE = True
except ImportError:
    IMAGE_PROCESSING_AVAILABLE = False
    print("⚠️  Image processing libraries not available - install pillow and numpy")

try:
    import pytesseract
    OCR_ENGINE = 'pytesseract'
except ImportError:
    try:
        import easyocr
        reader = easyocr.Reader(['en'])
        OCR_ENGINE = 'easyocr'
    except ImportError:
        OCR_ENGINE = None
        print("⚠️  OCR not available - install pytesseract or easyocr")


# Try to load config helper
try:
    from load_config import load_config, apply_config_to_automation
    CONFIG_LOADER_AVAILABLE = True
except ImportError:
    CONFIG_LOADER_AVAILABLE = False


class AndroidAutomation:
    """Android automation class for game automation"""
    
    def __init__(self, game_package_name=None):
        # Game package name (e.g., "com.example.game")
        # Leave None to use current foreground app
        self.game_package = game_package_name
        
        # Initialize device connection
        if USE_UIAUTOMATOR:
            try:
                # Connect to device - works standalone without computer!
                # Try local connection first (standalone mode)
                try:
                    self.device = u2.connect()  # Auto-detect device
                    print("✅ Connected via uiautomator2 (standalone mode)")
                except:
                    # Try connecting to localhost (for wireless ADB)
                    try:
                        self.device = u2.connect('127.0.0.1:5555')
                        print("✅ Connected via uiautomator2 (wireless ADB)")
                    except:
                        raise
            except Exception as e:
                print(f"⚠️  uiautomator2 connection failed: {e}")
                print("   Make sure uiautomator2 is initialized:")
                print("   Run: python -m uiautomator2 init")
                USE_UIAUTOMATOR = False
                self.device = None
        else:
            self.device = None
            print("⚠️  uiautomator2 not available")
            print("   Install it for standalone operation: pip install uiautomator2")
        
        # Screenshots directory
        self.screenshots_dir = Path("/sdcard/automation_screenshots")
        if not self.screenshots_dir.exists():
            try:
                self.screenshots_dir.mkdir(parents=True, exist_ok=True)
            except:
                # Fallback to app directory
                self.screenshots_dir = Path("screenshots")
                self.screenshots_dir.mkdir(exist_ok=True)
        
        # Screen dimensions (will be set after first screenshot)
        self.screen_width = None
        self.screen_height = None
        
        # ============================================
        # CONFIGURABLE VARIABLES - Edit these values
        # ============================================
        self.reset_target_amount = 10
        self.timer_threshold = 5
        self.amount_threshold = 20
        self.final_step_target = '20/30'
        self.click_delay = 1.0  # seconds
        self.reset_clicks_delay = 0.05  # seconds
        
        # Coordinates (adjust for your screen size)
        self.start_click_x = 150
        self.start_click_y = 375
        
        # Reset clicks
        self.reset_button_x = 260
        self.reset_button_y = 945
        self.reset_button2_x = 585
        self.reset_button2_y = 1013
        self.reset_button3_x = 260
        self.reset_button3_y = 845
        
        # Post-timer clicks
        self.post_timer_click1_x = 260
        self.post_timer_click1_y = 885
        self.post_timer_click2_x = 220
        self.post_timer_click2_y = 390
        
        # Button region
        self.button_x = 220
        self.button_y = 370
        self.button_width = 120
        self.button_height = 25
        
        # OCR regions
        self.ocr_above_x = 220
        self.ocr_above_y = 340
        self.ocr_above_width = 120
        self.ocr_above_height = 25
        
        self.ocr_second_x = 110
        self.ocr_second_y = 400
        self.ocr_second_width = 60
        self.ocr_second_height = 25
        
        # State
        self.running = False
        self.paused = False
        self.start_time = None
        self.pause_start_time = None
        self.total_paused_time = 0
        self.timer_check_time = None
        
        # Timer OCR region (will be set from config if available)
        self.timer_ocr_x = None
        self.timer_ocr_y = None
        self.timer_ocr_width = None
        self.timer_ocr_height = None
        
        # Load configuration from setup wizard if available
        if CONFIG_LOADER_AVAILABLE:
            config = load_config()
            if config:
                apply_config_to_automation(self, config)
    
    def switch_to_game(self):
        """Switch to the game app - works standalone without computer"""
        if not self.game_package:
            print("⚠️  No game package specified, using current app")
            return True
        
        try:
            if USE_UIAUTOMATOR and self.device:
                # Method 1: Use uiautomator2 (works standalone, no computer needed)
                try:
                    self.device.app_start(self.game_package)
                    print(f"✅ Opening game: {self.game_package}")
                    time.sleep(3)  # Wait for app to load
                    
                    # Verify app is in foreground
                    current_app = self.device.app_current()
                    if current_app.get('package') == self.game_package:
                        print(f"✅ Game is now in foreground!")
                        return True
                    else:
                        print(f"⚠️  App started but may not be in foreground")
                        print(f"   Current app: {current_app.get('package', 'unknown')}")
                        # Try bringing to front
                        self.device.app_start(self.game_package, stop=True)
                        time.sleep(2)
                        return True
                except Exception as e:
                    print(f"⚠️  uiautomator2 app_start failed: {e}")
                    # Try alternative method
                    pass
            
            # Method 2: Try using Android's am (Activity Manager) via shell
            # This works if you have shell access (root or ADB over network)
            try:
                # Try to launch app using am start
                result = subprocess.run(
                    ['sh', '-c', f'am start -n {self.game_package}/.MainActivity'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    print(f"✅ Opened game using am start")
                    time.sleep(3)
                    return True
            except:
                pass
            
            # Method 3: Try monkey command (if available)
            try:
                result = subprocess.run(
                    ['sh', '-c', f'monkey -p {self.game_package} -c android.intent.category.LAUNCHER 1'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    print(f"✅ Opened game using monkey")
                    time.sleep(3)
                    return True
            except:
                pass
            
            print(f"⚠️  Could not automatically open game")
            print(f"   Please manually open the game now")
            print(f"   Waiting 5 seconds...")
            time.sleep(5)
            return True  # Return True anyway, user can open manually
            
        except Exception as e:
            print(f"⚠️  Error opening game: {e}")
            print(f"   Please manually open the game")
            print(f"   Waiting 5 seconds...")
            time.sleep(5)
            return True
    
    def get_screen_size(self):
        """Get screen dimensions - works standalone"""
        if self.screen_width and self.screen_height:
            return {'width': self.screen_width, 'height': self.screen_height}
        
        try:
            if USE_UIAUTOMATOR and self.device:
                # Method 1: Use uiautomator2 (works standalone)
                info = self.device.info
                self.screen_width = info['displayWidth']
                self.screen_height = info['displayHeight']
            else:
                # Method 2: Try shell command (works if shell access available)
                try:
                    result = subprocess.run(
                        ['sh', '-c', 'wm size'],
                        capture_output=True,
                        text=True,
                        timeout=2
                    )
                    if result.returncode == 0:
                        # Parse output like "Physical size: 1080x1920"
                        size_str = result.stdout.split()[-1]
                        w, h = map(int, size_str.split('x'))
                        self.screen_width = w
                        self.screen_height = h
                except:
                    # Method 3: Get from screenshot
                    screenshot_path = self.take_screenshot()
                    if screenshot_path and os.path.exists(screenshot_path):
                        img = Image.open(screenshot_path)
                        self.screen_width = img.width
                        self.screen_height = img.height
        except Exception as e:
            print(f"⚠️  Could not get screen size: {e}")
            # Default values (will be updated from screenshot)
            self.screen_width = 1080
            self.screen_height = 1920
        
        return {'width': self.screen_width, 'height': self.screen_height}
    
    def click(self, x, y, delay=0):
        """Click at coordinates - works standalone"""
        try:
            if USE_UIAUTOMATOR and self.device:
                # Method 1: Use uiautomator2 (works standalone, no computer needed)
                self.device.click(x, y)
            else:
                # Method 2: Try shell command (works if shell access available)
                try:
                    subprocess.run(
                        ['sh', '-c', f'input tap {x} {y}'],
                        check=False,
                        timeout=2
                    )
                except:
                    print(f"⚠️  Click method not available - install uiautomator2 for best results")
                    return False
            
            if delay > 0:
                time.sleep(delay)
            return True
        except Exception as e:
            print(f"❌ Click failed at ({x}, {y}): {e}")
            return False
    
    def take_screenshot(self, output_path=None):
        """Take screenshot and return path - works standalone"""
        try:
            if output_path is None:
                timestamp = int(time.time() * 1000)
                output_path = self.screenshots_dir / f"screenshot_{timestamp}.png"
            
            if USE_UIAUTOMATOR and self.device:
                # Method 1: Use uiautomator2 (works standalone, no computer needed)
                self.device.screenshot(str(output_path))
            else:
                # Method 2: Try shell command (works if shell access available)
                try:
                    temp_path = "/sdcard/screenshot_temp.png"
                    # Take screenshot
                    subprocess.run(
                        ['sh', '-c', f'screencap -p {temp_path}'],
                        check=False,
                        timeout=5
                    )
                    # Copy to local path
                    if os.path.exists(temp_path):
                        import shutil
                        shutil.copy(temp_path, str(output_path))
                    else:
                        # Try direct path
                        output_path = Path(temp_path)
                except Exception as e:
                    print(f"⚠️  Screenshot via shell failed: {e}")
                    print(f"   Install uiautomator2 for better screenshot support")
                    return None
            
            # Update screen size from screenshot
            if IMAGE_PROCESSING_AVAILABLE and os.path.exists(output_path):
                img = Image.open(output_path)
                self.screen_width = img.width
                self.screen_height = img.height
            
            return str(output_path)
        except Exception as e:
            print(f"❌ Screenshot failed: {e}")
            return None
    
    def recognize_text(self, image_path, region=None):
        """Perform OCR on image or region"""
        if OCR_ENGINE is None:
            return {'text': '', 'confidence': 0}
        
        try:
            if not os.path.exists(image_path):
                return {'text': '', 'confidence': 0}
            
            img = Image.open(image_path)
            
            # Crop region if specified
            if region:
                x, y, w, h = region
                img = img.crop((x, y, x + w, y + h))
            
            # Preprocess image for better OCR (using PIL instead of opencv)
            if IMAGE_PROCESSING_AVAILABLE:
                # Convert to grayscale
                if img.mode != 'L':
                    img = img.convert('L')
                
                # Enhance contrast for better OCR
                enhancer = ImageEnhance.Contrast(img)
                img = enhancer.enhance(2.0)  # Increase contrast
                
                # Apply simple threshold (median-based, faster than Otsu)
                img_array = np.array(img)
                threshold = np.median(img_array)  # Use median as threshold
                
                # Apply threshold: values above threshold become white (255), below become black (0)
                img_array = np.where(img_array > threshold, 255, 0).astype(np.uint8)
                img = Image.fromarray(img_array)
            
            # Perform OCR
            if OCR_ENGINE == 'pytesseract':
                text = pytesseract.image_to_string(img, config='--psm 7 -c tessedit_char_whitelist=0123456789/:$')
                return {'text': text.strip(), 'confidence': 1.0}
            elif OCR_ENGINE == 'easyocr':
                results = reader.readtext(np.array(img))
                text = ' '.join([result[1] for result in results])
                return {'text': text.strip(), 'confidence': 1.0}
        except Exception as e:
            print(f"❌ OCR failed: {e}")
        
        return {'text': '', 'confidence': 0}
    
    def is_button_blue(self):
        """Check if button is blue by analyzing color"""
        if not IMAGE_PROCESSING_AVAILABLE:
            return False
        
        try:
            screenshot_path = self.take_screenshot()
            if not screenshot_path:
                return False
            
            img = Image.open(screenshot_path)
            # Crop button region
            button_img = img.crop((
                self.button_x,
                self.button_y,
                self.button_x + self.button_width,
                self.button_y + self.button_height
            ))
            
            # Convert to numpy array
            img_array = np.array(button_img)
            if len(img_array.shape) == 3:
                # Calculate average color
                avg_color = img_array.mean(axis=(0, 1))
                r, g, b = avg_color[:3]
                
                # Check if blue is dominant
                is_blue = b > 100 and b > r * 1.2 and b > g * 1.2
                return is_blue
        except Exception as e:
            print(f"❌ Button color check failed: {e}")
        
        return False
    
    def get_button_ocr_amount(self):
        """Get amount from button OCR"""
        try:
            screenshot_path = self.take_screenshot()
            if not screenshot_path:
                return None
            
            # Crop button region
            region = (self.button_x, self.button_y, self.button_width, self.button_height)
            ocr_result = self.recognize_text(screenshot_path, region)
            
            # Extract number from text
            import re
            match = re.search(r'\$?\s*(\d+)', ocr_result['text'])
            if match:
                return int(match.group(1))
        except Exception as e:
            print(f"❌ Get button amount failed: {e}")
        
        return None
    
    def reset_game(self):
        """Reset the game"""
        print("\n🔄 RESET: Starting reset process...")
        max_attempts = 50
        
        for attempt in range(1, max_attempts + 1):
            if not self.running:
                return False
            
            while self.paused and self.running:
                time.sleep(0.1)
            
            print(f"\n🔄 Reset attempt {attempt}/{max_attempts}")
            
            # Three reset clicks
            self.click(self.reset_button_x, self.reset_button_y, self.reset_clicks_delay)
            self.click(self.reset_button2_x, self.reset_button2_y, self.reset_clicks_delay)
            self.click(self.reset_button3_x, self.reset_button3_y, self.click_delay)
            
            # Click car
            self.click(self.start_click_x, self.start_click_y, self.click_delay)
            
            # Check button amount
            amount = self.get_button_ocr_amount()
            if amount is not None:
                print(f"   💰 Button amount: {amount}")
                if amount <= self.reset_target_amount:
                    print(f"   ✅ Reset successful! Amount: {amount}")
                    return True
            
            time.sleep(0.5)
        
        print("❌ Reset failed after max attempts")
        return False
    
    def format_elapsed_time(self, seconds):
        """Format elapsed time"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        
        if hours > 0:
            return f"{hours}h {minutes}m {secs}s"
        elif minutes > 0:
            return f"{minutes}m {secs}s"
        else:
            return f"{secs}s"
    
    def toggle_pause(self):
        """Toggle pause state"""
        if not self.running:
            return
        
        self.paused = not self.paused
        
        if self.paused:
            self.pause_start_time = time.time()
            print("\n⏸️  PAUSED - Press to resume")
        else:
            if self.pause_start_time:
                paused_duration = time.time() - self.pause_start_time
                self.total_paused_time += paused_duration
                if self.start_time:
                    self.start_time += paused_duration
                self.pause_start_time = None
            print("\n▶️  RESUMED")
    
    def run(self):
        """Main automation loop"""
        try:
            print("🔌 Initializing Android automation...")
            
            # Switch to game if package name is provided
            if self.game_package:
                print(f"\n📱 Switching to game: {self.game_package}")
                self.switch_to_game()
            else:
                print("\n⏳ Waiting 5 seconds for you to switch to the game...")
                print("   (Switch to your game app now!)")
                for i in range(5, 0, -1):
                    print(f"   Starting in {i}...")
                    time.sleep(1)
            
            self.get_screen_size()
            print(f"\n📱 Screen size: {self.screen_width}x{self.screen_height}\n")
            
            # Start with reset
            print("🔄 Starting with reset...\n")
            if not self.reset_game():
                print("❌ Reset failed. Cannot continue automation.")
                return
            
            # Verify button amount
            print("\n🔍 Verifying button amount after reset...")
            button_amount = self.get_button_ocr_amount()
            if button_amount is None or button_amount > self.reset_target_amount:
                print(f"❌ Button amount is {button_amount}, expected <= {self.reset_target_amount}")
                return
            
            print(f"✅ Button amount verified: {button_amount}. Starting automation...\n")
            
            self.start_time = time.time()
            self.running = True
            
            while self.running:
                # Check pause
                while self.paused and self.running:
                    time.sleep(0.1)
                
                if not self.running:
                    break
                
                # Click start button
                self.click(self.start_click_x, self.start_click_y, self.click_delay)
                
                # Check if button is blue/active
                is_blue = self.is_button_blue()
                
                if is_blue:
                    print("\n✅ BUTTON IS BLUE/ACTIVE!")
                    
                    # Click button
                    button_center_x = self.button_x + self.button_width // 2
                    button_center_y = self.button_y + self.button_height // 2
                    self.click(button_center_x, button_center_y, self.click_delay)
                    
                    # Perform OCR above button
                    screenshot_path = self.take_screenshot()
                    if screenshot_path:
                        region = (self.ocr_above_x, self.ocr_above_y, 
                                 self.ocr_above_width, self.ocr_above_height)
                        ocr_result = self.recognize_text(screenshot_path, region)
                        ocr_text = ocr_result['text']
                        
                        print(f"\n📝 OCR Result: \"{ocr_text}\"")
                        
                        # Check if final step
                        if self.final_step_target in ocr_text:
                            print(f"\n✅ Step is {self.final_step_target} - Automation complete!")
                            elapsed = time.time() - self.start_time
                            print(f"\n⏱️  Total time: {self.format_elapsed_time(elapsed)}")
                            self.running = False
                            return
                        
                        # Check if step is 10/20 - timer check
                        if '10/20' in ocr_text:
                            print("\n✅ Step is 10/20 - Checking timer...")
                            time.sleep(10)  # Wait before checking timer
                            
                            # Take screenshot for timer OCR
                            screenshot_path = self.take_screenshot()
                            # Timer OCR region (use config if available, otherwise default)
                            if self.timer_ocr_x is not None:
                                timer_region = (self.timer_ocr_x, self.timer_ocr_y,
                                              self.timer_ocr_width, self.timer_ocr_height)
                            else:
                                # Default: button region + offset
                                timer_region = (self.button_x + 30, self.button_y + 30,
                                              self.button_width - 30, self.button_height)
                            ocr_result = self.recognize_text(screenshot_path, timer_region)
                            timer_text = ocr_result['text']
                            
                            print(f"📝 Timer OCR: \"{timer_text}\"")
                            
                            # Extract timer seconds
                            import re
                            timer_match = re.search(r':(\d+)', timer_text)
                            if timer_match:
                                timer_seconds = int(timer_match.group(1))
                                print(f"⏱️  Timer seconds: {timer_seconds}")
                                
                                if timer_seconds > self.timer_threshold:
                                    print(f"⚠️  Timer is {timer_seconds} seconds (> {self.timer_threshold}), resetting...")
                                    self.reset_game()
                                    continue
                                else:
                                    # Log time from start
                                    if self.start_time:
                                        elapsed = time.time() - self.start_time
                                        print(f"⏱️  Time from start until timer check passed: {self.format_elapsed_time(elapsed)}")
                                    
                                    print(f"✅ Timer is {timer_seconds} seconds (<= {self.timer_threshold})")
                                    
                                    # Post-timer clicks
                                    self.click(self.start_click_x, self.start_click_y, self.click_delay)
                                    time.sleep(10)
                                    self.click(self.post_timer_click1_x, self.post_timer_click1_y, self.click_delay)
                                    time.sleep(self.click_delay)
                                    self.click(self.post_timer_click2_x, self.post_timer_click2_y, self.click_delay)
                                    time.sleep(self.click_delay)
                                    
                                    # Continue with blue button clicking only
                                    print("✅ Post-timer clicks completed. Now only clicking blue button...")
                                    time.sleep(self.click_delay * 2)
                                    
                                    while self.running:
                                        while self.paused and self.running:
                                            time.sleep(0.1)
                                        
                                        if not self.running:
                                            break
                                        
                                        if self.is_button_blue():
                                            print("\n✅ BUTTON IS BLUE/ACTIVE!")
                                            self.click(button_center_x, button_center_y, self.click_delay)
                                            
                                            # Check final step
                                            screenshot_path = self.take_screenshot()
                                            if screenshot_path:
                                                region = (self.ocr_above_x, self.ocr_above_y,
                                                         self.ocr_above_width, self.ocr_above_height)
                                                ocr_result = self.recognize_text(screenshot_path, region)
                                                if self.final_step_target in ocr_result['text']:
                                                    print(f"\n✅ Step is {self.final_step_target} - Automation complete!")
                                                    elapsed = time.time() - self.start_time
                                                    print(f"\n⏱️  Total time: {self.format_elapsed_time(elapsed)}")
                                                    self.running = False
                                                    return
                                        
                                        time.sleep(self.click_delay * 2)
                                    
                                    break
                        
                        # Check if step is 2/10
                        if '2/10' in ocr_text:
                            print("📍 Step is 2/10")
                            screenshot_path = self.take_screenshot()
                            if screenshot_path:
                                region = (self.ocr_second_x, self.ocr_second_y,
                                         self.ocr_second_width, self.ocr_second_height)
                                ocr_result = self.recognize_text(screenshot_path, region)
                                ocr_text2 = ocr_result['text']
                                print(f"\n📝 Second OCR Result: \"{ocr_text2}\"")
                                
                                # Extract amount
                                import re
                                amount_match = re.search(r'\$?\s*(\d+)', ocr_text2)
                                if amount_match:
                                    amount = int(amount_match.group(1))
                                    print(f"💰 Amount detected: {amount}")
                                    
                                    if amount < self.amount_threshold:
                                        print(f"⚠️  Amount {amount} < {self.amount_threshold}, resetting...")
                                        self.reset_game()
                                        continue
                
                time.sleep(self.click_delay)
        
        except KeyboardInterrupt:
            print("\n🛑 Stopping automation...")
            self.running = False
        except Exception as e:
            print(f"\n❌ Error: {e}")
            self.running = False
        finally:
            if self.start_time:
                elapsed = time.time() - self.start_time
                print(f"\n⏱️  Total time: {self.format_elapsed_time(elapsed)}")


if __name__ == "__main__":
    print("""
    ════════════════════════════════════════════════════════
    Android Game Automation Script
    ════════════════════════════════════════════════════════
    
    HOW TO USE:
    ════════════════════════════════════════════════════════
    
    Option 1: Automatic App Switching (Recommended)
    - Set your game package name below (e.g., "com.example.game")
    - The script will automatically switch to the game
    
    Option 2: Manual Switching
    - Leave game_package as None
    - Run the script, then quickly switch to your game
    - You'll have 5 seconds to switch
    
    To find your game package name:
    1. Open the game
    2. Run: adb shell dumpsys window | grep mCurrentFocus
    3. Look for the package name in the output
    
    ════════════════════════════════════════════════════════
    """)
    
    # ============================================
    # CONFIGURATION: Game package name
    # ============================================
    # Your game: Virtual Truck Manager 3
    GAME_PACKAGE = "com.virtualtruck.manager3"  # ✅ Set to your game!
    
    # ============================================
    
    automation = AndroidAutomation(game_package_name=GAME_PACKAGE)
    
    print("""
    Requirements:
    - ADB debugging enabled on your device
    - Required Python packages installed
    
    STANDALONE MODE (No Computer Needed!):
    ════════════════════════════════════════════════════
    
    To run completely standalone on your Android device:
    
    1. Install packages in Pydroid 3:
       - pillow, numpy, pytesseract (or easyocr)
       - uiautomator2 (REQUIRED for standalone mode!)
    
    2. Initialize uiautomator2 (ONE TIME SETUP):
       - In Pydroid 3, run: python -m uiautomator2 init
       - This installs an app on your device
       - Grant the necessary permissions when prompted
    
    3. Game package name is already set: com.virtualtruck.manager3
    
    4. Run the script - it will automatically open Virtual Truck Manager 3!
    
    ════════════════════════════════════════════════════
    
    Press Ctrl+C in Pydroid 3 to stop the automation
    ════════════════════════════════════════════════════════
    """)
    
    try:
        automation.run()
    except KeyboardInterrupt:
        print("\n\n✅ Automation stopped by user")
