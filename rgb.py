import os 
import sys

BRIGHTNESS_PATH = "/sys/class/leds/asus::kbd_backlight/brightness"

def check_path():
    if not os.path.exists(BRIGHTNESS_PATH):
        print("Error: Asus keyboard backlight path not found.")
        print("Make sure the 'asus-nb-wmi' kernel module is loaded.")
        sys.exit(1)

def set_brightness(level):
    try:
        command = f"echo {level} | sudo tee {BRIGHTNESS_PATH} > /dev/null"
        os.system(command)
        print(f"Successful set brightness to {level}!")
    except Exception as e:
        print(f"An error occured: {e}") 
        
if __name__ == "__main__":
    check_path()
    
    print(" == ASUS Linux Keyboard Controller ==")
    print("Enter a number from 0(Off) to 3(Max). Type 'q' to quit.")
    
    while True:
        user_input = input("\n Enter brightness level: ").strip()
        
        if user_input.lower() == 'q':
            print("Existing controller. Goodbye!")
            break
        
        if user_input.isdigit() and 0 <= int(user_input) <= 3:
            set_brightness(user_input)
        else:
            print("Invalid input. Please enter 0, 1, 2, 3, or 'q'.")
            