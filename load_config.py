"""
Helper module to load configuration from JSON file
Used by android-automation.py to load setup wizard config
"""

import json
from pathlib import Path


def load_config(config_file="automation_config.json"):
    """Load configuration from JSON file"""
    config_path = Path(config_file)
    
    if not config_path.exists():
        return None
    
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️  Error loading config: {e}")
        return None


def apply_config_to_automation(automation, config):
    """Apply loaded config to automation instance"""
    if not config:
        return
    
    # Start click
    if 'start_click' in config:
        automation.start_click_x = config['start_click']['x']
        automation.start_click_y = config['start_click']['y']
    
    # Button region
    if 'button' in config:
        automation.button_x = config['button']['x']
        automation.button_y = config['button']['y']
        automation.button_width = config['button']['width']
        automation.button_height = config['button']['height']
    
    # Reset clicks
    if 'reset_click_1' in config:
        automation.reset_button_x = config['reset_click_1']['x']
        automation.reset_button_y = config['reset_click_1']['y']
    
    if 'reset_click_2' in config:
        automation.reset_button2_x = config['reset_click_2']['x']
        automation.reset_button2_y = config['reset_click_2']['y']
    
    if 'reset_click_3' in config:
        automation.reset_button3_x = config['reset_click_3']['x']
        automation.reset_button3_y = config['reset_click_3']['y']
    
    # Post-timer clicks
    if 'post_timer_click_1' in config:
        automation.post_timer_click1_x = config['post_timer_click_1']['x']
        automation.post_timer_click1_y = config['post_timer_click_1']['y']
    
    if 'post_timer_click_2' in config:
        automation.post_timer_click2_x = config['post_timer_click_2']['x']
        automation.post_timer_click2_y = config['post_timer_click_2']['y']
    
    # OCR regions
    if 'ocr_above' in config:
        automation.ocr_above_x = config['ocr_above']['x']
        automation.ocr_above_y = config['ocr_above']['y']
        automation.ocr_above_width = config['ocr_above']['width']
        automation.ocr_above_height = config['ocr_above']['height']
    
    if 'ocr_second' in config:
        automation.ocr_second_x = config['ocr_second']['x']
        automation.ocr_second_y = config['ocr_second']['y']
        automation.ocr_second_width = config['ocr_second']['width']
        automation.ocr_second_height = config['ocr_second']['height']
    
    # Timer OCR
    if 'timer_ocr' in config:
        automation.timer_ocr_x = config['timer_ocr']['x']
        automation.timer_ocr_y = config['timer_ocr']['y']
        automation.timer_ocr_width = config['timer_ocr']['width']
        automation.timer_ocr_height = config['timer_ocr']['height']
    
    # Thresholds
    if 'reset_target_amount' in config:
        automation.reset_target_amount = config['reset_target_amount']
    
    if 'timer_threshold' in config:
        automation.timer_threshold = config['timer_threshold']
    
    if 'amount_threshold' in config:
        automation.amount_threshold = config['amount_threshold']
    
    if 'final_step_target' in config:
        automation.final_step_target = config['final_step_target']
    
    print("✅ Configuration loaded from setup wizard!")
