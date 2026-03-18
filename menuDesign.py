#modeule  : menuDesign.py
#auther   : LING KS's students
#date     : 18-03-2026
#purpose  : design and maintain main menu
#import   : os(system),time
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

def main_menu(data):
    w_lines=wt.get_dashboard_lines(data)
    title = "MAIN MENU"
    options = ["1.Admin Management", "2.Estimate travel time", "3.Help Centre", "4.Exit"]
    print("=" * 70)
    print(f"{title:^70}")
    print("=" * 70)
    for i in range(4):
        # weather_line (30 chars) + Gap + Menu Option
        indent=2 if i%2 != 0 else 0
        base_width=50
        spacer=" "*indent
        option_text=f"♦ {options[i]}"
        weather_text = f"{w_lines[i]}"
        weather_part=f"{weather_text}"
        option_part = f"{spacer}{option_text:<{base_width-indent}}"
        print(f"{option_part}|{weather_part}")
    
    print("=" * 70)
