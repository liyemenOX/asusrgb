Asus Linux Keyboard Backlight Controller
  A lightweight Python CLI utility to manage the RGB color and brightness of Asus laptop keyboard backlights on Linux. 
  It directly interfaces with the kernel sysfs attributes to provide quick, native hardware control without heavy background daemons.
  
Features:
  Brightness Control: Toggle backlight intensity across 4 distinct levels (0 to 3).
  RGB Color Palette: Instantly switch between 8 pre-configured vibrant colors.
  Native Integration: Uses secure system pipelines via standard kernel modules.
  PrerequisitesOperating System: Linux distributions running on an Asus laptop.
  Kernel Module: Ensure the asus-nb-wmi module is loaded.

Permissions: You need sudo privileges to modify kernel hardware paths.

Installation & SetupClone this repository or download the script file.

Ensure the script has executable permissions:bashchmod +x main.py

Use code with caution.UsageRun the script using Python 3:bashpython3 main.py
Use code with caution.Script InterfaceThe interactive command-line interface prompts you with the following main options:

                        =======================================
                          ASUS LINUX HARDWARE CONTROLLER     
                        =======================================

[1] Change Brightness (0-3)
[2] Change Keyboard color
[Q] Quit Application
Use code with caution.

How It Works
  The script operates by securely writing configuration strings to the following Linux sysfs attributes:
  Brightness: /sys/class/leds/asus::kbd_backlight/brightnessRGB 
  Mode: /sys/class/leds/asus::kbd_backlight/kbd_rgb_modeColor data is sent using the kernel 
  format: "cmd mode red green blue speed".
  TroubleshootingIf you encounter the error Asus keyboard backlight path not found, resolve it by forcing the kernel driver to 
  load:bashsudo modprobe asus-nb-wmi
