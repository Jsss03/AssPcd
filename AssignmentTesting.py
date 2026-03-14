import os
import math
import time

FILENAME="location.txt"
default_routes=[["KLCC","Bangsar Shopping mall","6.5"],\
["UTAR-SL","Mid Valley","25.6"],["UTAR-SL","Sunway Pyramid","30"],["TARUMT","Pavillion","15.2"],["UTAR-SL","Sunway Velocity","20"]]

def sync_defaults():
    existing_lines=[]
    if os.path.exists(FILENAME):
        with open (FILENAME,"r") as f:
            existing_lines=[line.strip() for line in f if line.strip()]
            with open(FILENAME,"a") as f:
                for route in default_routes:
                    route_str="|".join(route)
                    if route_str not in existing_lines:
                        f.write(route_str + "\n")

def load_matrix():
    matrix=[]
    if os.path.exists(FILENAME):
        with open(FILENAME,"r")as f:
            for line in f:
                if line.strip():
                    matrix.append(line.strip().split("|"))
    return matrix

sync_defaults()
location_matirx=load_matrix()
for row in location_matirx:
    

def clear_screen():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def function1():
    while True:
        clear_screen()
        print("1.Run this function")
        print("2.Exit to main menu")

        sub_choice=input("Please choose 1-2 >> ")
        if sub_choice=='1':
            print("Run successfully!")
            input("Press ANY to proceed.")
            clear_screen()
            break
        elif sub_choice=='2':
            clear_screen()
            break

def boot_sequence():
    print("Loading Main Menu...")
    for i in range(21):
        percent = i * 5
        bar = "█" * i + "-" * (20 - i)
        print(f"\r|{bar}| {percent}%", end="")
        time.sleep(0.1)
    print("\n\n--- ACCESS GRANTED ---\n")

def wave_menu():
    title = "MAIN MENU"
    options = ["1.Admin", "2.Estimate", "3.Exit"]
    
    # 1. Display the Title (Stationary)
    print(f"\n{'='*60}")
    print(f"{title:^60}")
    print(f"{'='*60}\n")

    # 2. Display the Waving Options
    for i, opt in enumerate(options):
        # The Logic:
        # Base offset of 5 spaces + a sine curve that moves up to 4 spaces
        indent_size = int(5 + 4 * math.sin(i * 1.5))
        
        indent = " " * indent_size
        print(f"{indent}◈ {opt}")
    print("")
    print(f"{'='*60}\n")
def main_menu():
    running=True
    has_booted=False

    while running:
        if not has_booted:
            boot_sequence()
            input("Press ANY to continue..")
            clear_screen()
            has_booted = True 
        wave_menu()
        choice=input("Please choose(1-3)>>")
        if choice=='1':
            clear_screen()
            function1()
        elif choice=='2':
            clear_screen()
            print("Function2")
            input("Press Enter to continue...")
            clear_screen()
        elif choice=='3':
            clear_screen()
            print("Exiting...")
            running=False
        else:
            print("Unavailable choice.Please try again")

if __name__=="__main__":
    main_menu()
