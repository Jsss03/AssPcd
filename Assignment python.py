import os
import math
import time
from tkinter import Place

def clear_screen():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def function1():
    location = ["Japan", "China", "Taiwan", "Singapore","Malaysia"]
    print(location)

    while True:
        
        clear_screen()

        print("1.Run this function")
        print("2.Exit to main menu")

        sub_choice=input("Please choose 1-2 >> ")
        if sub_choice=='1':
            print("Run successfully!")
            location = ["Japan", "China", "Taiwan", "Singapore","Malaysia","Indonesia"]
            n = len(location)
            w = 12
            matrix = [[0]*n for i in range(n)]
            print("".ljust(w), end="")
            for name in location:
                print(name.ljust(w), end="")
            print()
            for i in range(n):
                print(location[i].ljust(w), end="")
                for j in range(n):
                    print(str(matrix[i][j]).ljust(w), end="")
                print()
                

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







