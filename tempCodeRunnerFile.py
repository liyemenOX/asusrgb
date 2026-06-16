import os 
import sys

BRIGHTNESS_PATH = "/sys/class/leds/asus::kbd_backlight/brightness"

def check_path():
    if not os.path.exists(BRIGHTNESS_PATH):
        print("Error: Asus keyboard backlight path not found.")
        print("Make sure the 'asus-nb-wmi' kernel module is loaded.")
        sys.exit(1)