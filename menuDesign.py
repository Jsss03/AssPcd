#modeule  : menuDesign.py
#auther   : Group 3
#date     : 18-03-2026
#purpose  : design and maintain main menu
#import   : os(system),time,DFweathers
#amendment:

import os
import time
import DFweathers as wt

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
def boot_sequence():
    print("Loading Main Menu...")
    for i in range(21):
        percent = i * 5
        bar = "█" * i + "-" * (20 - i)
        print(f"\r|{bar}| {percent}%", end="")
        time.sleep(0.1)
    print("\n\n--- ACCESS GRANTED ---\n")

def main_menu(data, role="admin"):
    w_lines=wt.get_dashboard_lines(data)
    title = "MAIN MENU"
    # if/else: pick options list based on role
    if role == "admin":
        options = ["1.Admin Management", "2.Estimate travel time", "3.Help Centre", "4.Exit"]
    else:                                          # guest: no Admin Management
        options = ["1.Estimate travel time", "2.Help Centre", "3.Exit"]
    print("=" * 70)
    print(f"{title:^70}")
    print("=" * 70)
    for i in range(max(len(options),len(w_lines))):
        indent=2 if i%2 != 0 else 0
        base_width=50
        spacer=" "*indent
        current_option=options[i] if i< len(options) else ""
        option_text=f"♦ {current_option}"if current_option else ""
        weather_text = f"{w_lines[i]}" if i < len(w_lines) else ""
        weather_part=f"{weather_text}"
        option_part = f"{spacer}{option_text:<{base_width-indent}}"
        print(f"{option_part}|{weather_part}")
    
    print("=" * 70)
