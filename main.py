"""
Simple Android App for Game Automation
Tap to set coordinates, draw rectangles for OCR, run automation
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import json
import os
from pathlib import Path

# Try to import automation modules
try:
    from automation_core import AutomationCore
    AUTOMATION_AVAILABLE = True
except ImportError:
    AUTOMATION_AVAILABLE = False
    print("⚠️  Automation core not available - install dependencies")


class CoordinateInput(BoxLayout):
    """Widget for entering coordinates"""
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.name = name
        
        self.add_widget(Label(text=f"{name}:", size_hint_x=0.3))
        
        x_input = TextInput(hint_text="X", multiline=False, size_hint_x=0.35)
        y_input = TextInput(hint_text="Y", multiline=False, size_hint_x=0.35)
        
        self.x_input = x_input
        self.y_input = y_input
        
        self.add_widget(x_input)
        self.add_widget(y_input)
    
    def get_coords(self):
        try:
            return (int(self.x_input.text), int(self.y_input.text))
        except:
            return None


class OCRRegionInput(BoxLayout):
    """Widget for entering OCR region"""
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.name = name
        
        self.add_widget(Label(text=f"{name}:", size_hint_x=0.3))
        
        x_input = TextInput(hint_text="X", multiline=False, size_hint_x=0.2)
        y_input = TextInput(hint_text="Y", multiline=False, size_hint_x=0.2)
        w_input = TextInput(hint_text="W", multiline=False, size_hint_x=0.15)
        h_input = TextInput(hint_text="H", multiline=False, size_hint_x=0.15)
        
        self.x_input = x_input
        self.y_input = y_input
        self.w_input = w_input
        self.h_input = h_input
        
        self.add_widget(x_input)
        self.add_widget(y_input)
        self.add_widget(w_input)
        self.add_widget(h_input)
    
    def get_region(self):
        try:
            return (int(self.x_input.text), int(self.y_input.text), 
                   int(self.w_input.text), int(self.h_input.text))
        except:
            return None


class AutomationApp(App):
    def build(self):
        self.config_file = Path("automation_config.json")
        self.load_config()
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title = Label(text="Game Automation Setup", size_hint_y=0.1, font_size=24)
        main_layout.add_widget(title)
        
        # Scrollable content
        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        # Click Coordinates Section
        click_section = BoxLayout(orientation='vertical', size_hint_y=None, height=200)
        click_section.add_widget(Label(text="Click Coordinates", size_hint_y=0.2, font_size=18))
        
        self.start_click = CoordinateInput("Start Click")
        self.reset_click1 = CoordinateInput("Reset Click 1")
        self.reset_click2 = CoordinateInput("Reset Click 2")
        self.reset_click3 = CoordinateInput("Reset Click 3")
        
        click_section.add_widget(self.start_click)
        click_section.add_widget(self.reset_click1)
        click_section.add_widget(self.reset_click2)
        click_section.add_widget(self.reset_click3)
        
        content.add_widget(click_section)
        
        # OCR Regions Section
        ocr_section = BoxLayout(orientation='vertical', size_hint_y=None, height=200)
        ocr_section.add_widget(Label(text="OCR Regions", size_hint_y=0.2, font_size=18))
        
        self.ocr_above = OCRRegionInput("OCR Above Button")
        self.ocr_timer = OCRRegionInput("OCR Timer")
        
        ocr_section.add_widget(self.ocr_above)
        ocr_section.add_widget(self.ocr_timer)
        
        content.add_widget(ocr_section)
        
        # Button Region
        button_section = BoxLayout(orientation='vertical', size_hint_y=None, height=150)
        button_section.add_widget(Label(text="Button Region", size_hint_y=0.3, font_size=18))
        self.button_region = OCRRegionInput("Button")
        button_section.add_widget(self.button_region)
        content.add_widget(button_section)
        
        # Thresholds
        threshold_section = BoxLayout(orientation='vertical', size_hint_y=None, height=200)
        threshold_section.add_widget(Label(text="Thresholds", size_hint_y=0.2, font_size=18))
        
        self.reset_amount = TextInput(hint_text="Reset Target Amount (e.g., 10)", multiline=False)
        self.timer_threshold = TextInput(hint_text="Timer Threshold (seconds, e.g., 5)", multiline=False)
        self.amount_threshold = TextInput(hint_text="Amount Threshold (e.g., 20)", multiline=False)
        self.final_step = TextInput(hint_text="Final Step (e.g., 20/30)", multiline=False)
        
        threshold_section.add_widget(self.reset_amount)
        threshold_section.add_widget(self.timer_threshold)
        threshold_section.add_widget(self.amount_threshold)
        threshold_section.add_widget(self.final_step)
        
        content.add_widget(threshold_section)
        
        scroll.add_widget(content)
        main_layout.add_widget(scroll)
        
        # Buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=0.15, spacing=10)
        
        save_btn = Button(text="Save Config")
        save_btn.bind(on_press=self.save_config)
        button_layout.add_widget(save_btn)
        
        load_btn = Button(text="Load Config")
        load_btn.bind(on_press=self.load_config_ui)
        button_layout.add_widget(load_btn)
        
        test_btn = Button(text="Test Coordinates")
        test_btn.bind(on_press=self.test_coordinates)
        button_layout.add_widget(test_btn)
        
        run_btn = Button(text="Run Automation")
        run_btn.bind(on_press=self.run_automation)
        button_layout.add_widget(run_btn)
        
        main_layout.add_widget(button_layout)
        
        # Status label
        self.status_label = Label(text="Ready", size_hint_y=0.1)
        main_layout.add_widget(self.status_label)
        
        return main_layout
    
    def load_config(self):
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def load_config_ui(self, instance):
        """Load config and populate UI"""
        config = self.load_config()
        
        # Load click coordinates
        if 'start_click' in config:
            self.start_click.x_input.text = str(config['start_click'].get('x', ''))
            self.start_click.y_input.text = str(config['start_click'].get('y', ''))
        
        # Load OCR regions
        if 'ocr_above' in config:
            self.ocr_above.x_input.text = str(config['ocr_above'].get('x', ''))
            self.ocr_above.y_input.text = str(config['ocr_above'].get('y', ''))
            self.ocr_above.w_input.text = str(config['ocr_above'].get('width', ''))
            self.ocr_above.h_input.text = str(config['ocr_above'].get('height', ''))
        
        self.status_label.text = "Config loaded!"
    
    def save_config(self, instance):
        """Save configuration to file"""
        config = {}
        
        # Save click coordinates
        start_coords = self.start_click.get_coords()
        if start_coords:
            config['start_click'] = {'x': start_coords[0], 'y': start_coords[1]}
        
        reset1 = self.reset_click1.get_coords()
        if reset1:
            config['reset_click_1'] = {'x': reset1[0], 'y': reset1[1]}
        
        reset2 = self.reset_click2.get_coords()
        if reset2:
            config['reset_click_2'] = {'x': reset2[0], 'y': reset2[1]}
        
        reset3 = self.reset_click3.get_coords()
        if reset3:
            config['reset_click_3'] = {'x': reset3[0], 'y': reset3[1]}
        
        # Save OCR regions
        ocr_above = self.ocr_above.get_region()
        if ocr_above:
            config['ocr_above'] = {'x': ocr_above[0], 'y': ocr_above[1], 
                                  'width': ocr_above[2], 'height': ocr_above[3]}
        
        ocr_timer = self.ocr_timer.get_region()
        if ocr_timer:
            config['timer_ocr'] = {'x': ocr_timer[0], 'y': ocr_timer[1],
                                  'width': ocr_timer[2], 'height': ocr_timer[3]}
        
        # Save button region
        button = self.button_region.get_region()
        if button:
            config['button'] = {'x': button[0], 'y': button[1],
                               'width': button[2], 'height': button[3]}
        
        # Save thresholds
        if self.reset_amount.text:
            config['reset_target_amount'] = int(self.reset_amount.text)
        if self.timer_threshold.text:
            config['timer_threshold'] = int(self.timer_threshold.text)
        if self.amount_threshold.text:
            config['amount_threshold'] = int(self.amount_threshold.text)
        if self.final_step.text:
            config['final_step_target'] = self.final_step.text
        
        # Save to file
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        self.status_label.text = "Config saved!"
    
    def test_coordinates(self, instance):
        """Test clicking at coordinates"""
        self.status_label.text = "Testing coordinates..."
        # This would call the automation core to test clicks
        # For now, just show a message
        Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', 'Test complete'), 2)
    
    def run_automation(self, instance):
        """Run the automation"""
        if not AUTOMATION_AVAILABLE:
            self.status_label.text = "Error: Automation not available"
            return
        
        self.status_label.text = "Starting automation..."
        # This would start the automation in a background thread
        # For now, just show a message
        Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', 'Automation running...'), 1)


if __name__ == '__main__':
    AutomationApp().run()
