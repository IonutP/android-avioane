"""
Overlay App for Game Automation
Runs as a floating overlay on top of the game
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle, Line
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform
import json
from pathlib import Path

# Android-specific imports
if platform == 'android':
    from android.permissions import request_permissions, Permission
    from android import api_version
    from jnius import autoclass, PythonJavaClass, java_method
    from android.runnable import run_on_ui_thread
    
    # Android classes
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    WindowManager = autoclass('android.view.WindowManager')
    LayoutParams = autoclass('android.view.WindowManager$LayoutParams')
    Gravity = autoclass('android.view.Gravity')
    Context = autoclass('android.content.Context')
    Intent = autoclass('android.content.Intent')
    Settings = autoclass('android.provider.Settings')


class OverlayButton(Button):
    """Floating button for overlay"""
    pass


class OCRRectangle:
    """Represents an OCR region rectangle"""
    def __init__(self, x, y, width, height, name=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.active = False


class OverlayApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config_file = Path("automation_config.json")
        self.ocr_rectangles = []
        self.drawing_rectangle = False
        self.rect_start = None
        self.current_rect = None
        self.overlay_mode = False
        
    def build(self):
        # Request overlay permission on Android
        if platform == 'android':
            self.request_overlay_permission()
        
        # Create overlay layout
        self.root = FloatLayout()
        
        # Semi-transparent background
        with self.root.canvas.before:
            Color(0, 0, 0, 0.3)  # Semi-transparent black
            self.bg_rect = Rectangle(size=Window.size, pos=(0, 0))
        
        # Control panel (collapsible)
        self.create_control_panel()
        
        # Bind window resize
        Window.bind(on_resize=self.on_window_resize)
        
        return self.root
    
    def request_overlay_permission(self):
        """Request overlay permission on Android"""
        if platform == 'android' and api_version >= 23:
            if not Settings.canDrawOverlays(PythonActivity.mActivity):
                intent = Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION)
                PythonActivity.mActivity.startActivity(intent)
    
    def create_control_panel(self):
        """Create the control panel overlay"""
        # Main control button (always visible)
        self.main_button = OverlayButton(
            text="⚙️",
            size_hint=(None, None),
            size=(60, 60),
            pos=(Window.width - 70, Window.height - 70)
        )
        self.main_button.bind(on_press=self.toggle_panel)
        self.root.add_widget(self.main_button)
        
        # Control panel (hidden by default)
        self.panel = FloatLayout(size_hint=(0.8, 0.6), pos=(Window.width * 0.1, Window.height * 0.2))
        self.panel.opacity = 0
        self.panel.disabled = True
        
        # Panel background
        with self.panel.canvas.before:
            Color(0.2, 0.2, 0.2, 0.95)
            self.panel_bg = Rectangle(size=self.panel.size, pos=self.panel.pos)
        
        # Panel title
        title = Label(
            text="Game Automation Overlay",
            size_hint=(1, 0.15),
            pos_hint={'x': 0, 'y': 0.85},
            font_size=20
        )
        self.panel.add_widget(title)
        
        # Close button
        close_btn = Button(
            text="✕",
            size_hint=(0.1, 0.1),
            pos_hint={'x': 0.9, 'y': 0.9}
        )
        close_btn.bind(on_press=self.toggle_panel)
        self.panel.add_widget(close_btn)
        
        # Buttons
        buttons = [
            ("Draw OCR Region", self.start_drawing_rect),
            ("Set Click Point", self.set_click_point),
            ("Save Config", self.save_config),
            ("Load Config", self.load_config),
            ("Run Automation", self.run_automation),
            ("Clear Rectangles", self.clear_rectangles),
        ]
        
        for i, (text, callback) in enumerate(buttons):
            btn = Button(
                text=text,
                size_hint=(0.45, 0.12),
                pos_hint={'x': 0.05 + (i % 2) * 0.5, 'y': 0.7 - (i // 2) * 0.15}
            )
            btn.bind(on_press=callback)
            self.panel.add_widget(btn)
        
        # Status label
        self.status_label = Label(
            text="Ready",
            size_hint=(1, 0.1),
            pos_hint={'x': 0, 'y': 0.05},
            font_size=14
        )
        self.panel.add_widget(self.status_label)
        
        self.root.add_widget(self.panel)
    
    def toggle_panel(self, instance):
        """Show/hide control panel"""
        if self.panel.opacity == 0:
            self.panel.opacity = 1
            self.panel.disabled = False
            self.main_button.text = "✕"
        else:
            self.panel.opacity = 0
            self.panel.disabled = True
            self.main_button.text = "⚙️"
    
    def on_window_resize(self, window, width, height):
        """Update background and button positions on resize"""
        self.bg_rect.size = (width, height)
        self.main_button.pos = (width - 70, height - 70)
        if hasattr(self, 'panel_bg'):
            self.panel.size_hint_x = 0.8
            self.panel.pos = (width * 0.1, height * 0.2)
            self.panel_bg.size = self.panel.size
            self.panel_bg.pos = self.panel.pos
    
    def start_drawing_rect(self, instance):
        """Start drawing OCR rectangle"""
        self.status_label.text = "Touch and drag to draw OCR region"
        self.drawing_rectangle = True
        self.rect_start = None
        Window.bind(on_touch_down=self.on_touch_down_rect)
        Window.bind(on_touch_move=self.on_touch_move_rect)
        Window.bind(on_touch_up=self.on_touch_up_rect)
    
    def on_touch_down_rect(self, window, touch):
        """Handle touch down for rectangle drawing"""
        if self.drawing_rectangle:
            self.rect_start = (touch.x, touch.y)
            # Create rectangle preview
            with self.root.canvas:
                Color(1, 0, 0, 0.5)  # Red, semi-transparent
                self.current_rect = Rectangle(
                    pos=self.rect_start,
                    size=(0, 0)
                )
            return True
        return False
    
    def on_touch_move_rect(self, window, touch):
        """Handle touch move for rectangle drawing"""
        if self.drawing_rectangle and self.rect_start and self.current_rect:
            width = touch.x - self.rect_start[0]
            height = touch.y - self.rect_start[1]
            self.current_rect.size = (abs(width), abs(height))
            if width < 0:
                self.current_rect.pos = (touch.x, self.current_rect.pos[1])
            if height < 0:
                self.current_rect.pos = (self.current_rect.pos[0], touch.y)
            return True
        return False
    
    def on_touch_up_rect(self, window, touch):
        """Handle touch up for rectangle drawing"""
        if self.drawing_rectangle and self.rect_start:
            width = abs(touch.x - self.rect_start[0])
            height = abs(touch.y - self.rect_start[1])
            x = min(touch.x, self.rect_start[0])
            y = min(touch.y, self.rect_start[1])
            
            # Save rectangle
            rect = OCRRectangle(x, y, width, height, f"OCR_{len(self.ocr_rectangles)}")
            self.ocr_rectangles.append(rect)
            
            # Draw permanent rectangle
            with self.root.canvas:
                Color(0, 1, 0, 0.3)  # Green, semi-transparent
                Rectangle(pos=(x, y), size=(width, height))
                Color(0, 1, 0, 1)  # Green border
                Line(rectangle=(x, y, width, height), width=2)
            
            # Clean up
            if self.current_rect:
                self.root.canvas.remove(self.current_rect)
                self.current_rect = None
            
            self.drawing_rectangle = False
            Window.unbind(on_touch_down=self.on_touch_down_rect)
            Window.unbind(on_touch_move=self.on_touch_move_rect)
            Window.unbind(on_touch_up=self.on_touch_up_rect)
            
            self.status_label.text = f"OCR region saved: ({int(x)}, {int(y)}, {int(width)}, {int(height)})"
            return True
        return False
    
    def set_click_point(self, instance):
        """Set a click coordinate by tapping"""
        self.status_label.text = "Tap on screen to set click point"
        Window.bind(on_touch_down=self.on_touch_down_click)
    
    def on_touch_down_click(self, window, touch):
        """Handle touch for setting click point"""
        # Don't capture if touching the panel or button
        if self.panel.collide_point(*touch.pos) or self.main_button.collide_point(*touch.pos):
            return False
        
        x, y = int(touch.x), int(touch.y)
        
        # Draw a marker
        with self.root.canvas:
            Color(1, 1, 0, 1)  # Yellow
            Line(circle=(x, y, 10), width=3)
        
        self.status_label.text = f"Click point set: ({x}, {y})"
        
        # Save to config (you can expand this)
        self.last_click_point = (x, y)
        
        Window.unbind(on_touch_down=self.on_touch_down_click)
        return True
    
    def clear_rectangles(self, instance):
        """Clear all drawn rectangles"""
        self.ocr_rectangles = []
        # Clear canvas (keep background)
        self.root.canvas.clear()
        with self.root.canvas.before:
            Color(0, 0, 0, 0.3)
            self.bg_rect = Rectangle(size=Window.size, pos=(0, 0))
        self.status_label.text = "Rectangles cleared"
    
    def save_config(self, instance):
        """Save configuration"""
        config = {
            'ocr_regions': [
                {
                    'x': rect.x,
                    'y': rect.y,
                    'width': rect.width,
                    'height': rect.height,
                    'name': rect.name
                }
                for rect in self.ocr_rectangles
            ]
        }
        
        if hasattr(self, 'last_click_point'):
            config['last_click_point'] = {
                'x': self.last_click_point[0],
                'y': self.last_click_point[1]
            }
        
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        self.status_label.text = "Config saved!"
    
    def load_config(self, instance):
        """Load configuration"""
        if not self.config_file.exists():
            self.status_label.text = "No config file found"
            return
        
        with open(self.config_file, 'r') as f:
            config = json.load(f)
        
        # Load OCR regions
        if 'ocr_regions' in config:
            self.clear_rectangles(None)
            for region in config['ocr_regions']:
                rect = OCRRectangle(
                    region['x'], region['y'],
                    region['width'], region['height'],
                    region.get('name', '')
                )
                self.ocr_rectangles.append(rect)
                
                # Redraw
                with self.root.canvas:
                    Color(0, 1, 0, 0.3)
                    Rectangle(pos=(rect.x, rect.y), size=(rect.width, rect.height))
                    Color(0, 1, 0, 1)
                    Line(rectangle=(rect.x, rect.y, rect.width, rect.height), width=2)
        
        self.status_label.text = "Config loaded!"
    
    def run_automation(self, instance):
        """Run the automation"""
        self.status_label.text = "Starting automation..."
        # This would start the automation core
        # For now, just show status
        Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', 'Automation running...'), 1)


if __name__ == '__main__':
    OverlayApp().run()
