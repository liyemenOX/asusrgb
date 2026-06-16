import os 
import sys

BRIGHTNESS_PATH = "/sys/class/leds/asus::kbd_backlight/brightness"
RGB_PATH = "/sys/class/leds/asus::kbd_backlight/kbd_rgb_mode"

def check_path():
    if not os.path.exists(BRIGHTNESS_PATH):
        print("Error: Asus keyboard backlight path not found.")
        print("Make sure the 'asus-nb-wmi' kernel module is loaded.")
        sys.exit(1)
        
def set_color(r, g, b):
    try:
        # FORMAT: "cmd mode red green blue speed"
        # cmd: 0 (don't save to flash) or 1 (save to firmware)
        # mode: 0 (Static)
        # speed: 0 (Slow), 1 (Medium), 2 (Fast) - doesn't matter for static
        
        color_string = f"0 0 {r} {g} {b} 0"
        
        command = f"echo '{color_string}' | sudo tee {RGB_PATH} > /dev/null"
        os.system(command)
        print(f"Success! Color set to RGB({r}, {g}, {b})")       
    except Exception as e:
        print(f"Error changing color: {e}")

COLOR_PALETTE = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "white": (255, 255, 255),
    "orange": (255, 165, 0)
}

def set_brightness(level):
    try:
        command = f"echo {level} | sudo tee {BRIGHTNESS_PATH} > /dev/null"
        os.system(command)
        print(f"Successful set brightness to {level}!")
    except Exception as e:
        print(f"An error occured: {e}") 
        
if __name__ == "__main__":
    check_path()
    
    print("=======================================")
    print("    ASUS LINUX HARDWARE CONTROLLER     ")
    print("=======================================")
    
    while True:
        print("\n[1] Change Brightness (0-3)")
        print("[2] Change Keyboard color")
        print("[Q] Quit Application")
    
        choice  = input("\nSelect an option: ").strip().lower()
    
        if choice.lower() == 'q':
            print("Existing controller. Goodbye!")
            break
        
        elif choice == '1':
            level = input("\n Enter brightness level: ").strip()
        
        
            if level.isdigit() and 0 <= int(level) <= 3:
                set_brightness(level)
            else:
                print("Invalid input. Please enter 0, 1, 2, 3, or 'q'.")
    
    # Part 4: Connecting them together
        elif choice == '2':
            print(f"Available colors: {', '.join(COLOR_PALETTE.keys())}")
            user_choice = input("Enter color: ").strip().lower()

            if user_choice in COLOR_PALETTE:
                r, g, b = COLOR_PALETTE[user_choice]
                set_color(r, g, b)
            else:
                print("color not found in a palette")       
            
        else:
            print("Invalid option. Please choose 1, 2, or Q.")  