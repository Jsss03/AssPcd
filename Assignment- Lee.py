import os
import math
import time


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def function1():
    while True:
        clear_screen()
        print("1.Run this function")
        print("2.Exit to main menu")

        sub_choice = input("Please choose 1-2 >> ")
        if sub_choice == '1':
            print("Run successfully!")
            input("Press ANY to proceed.")
            clear_screen()
            break
        elif sub_choice == '2':
            clear_screen()
            break
locations = ["Central Park", "City Hall", "Museum", "Shopping Mall", "Train Station "]
distance_matrix = [[0, 1, 2.5, 4.0, 3.2, 5.1], [2.5,0,3.1,2.0,4.2],[4.0,3.1,0,2.8,3.5],[3.2,2.0,2.8,0,3.0],[5.1,4.2,3.5,3.0,0]]
transport_modes = {"walking":5,"bicycle":15,"car":60,"bus":40}
time_multiplier = {"morning":0.75,"afternoon":1.0,"evening":0.7,"night":1.15}
season_multiplier ={"normal":1.0,"rainy":0.85,"festive_holiday":0.80}
traffic_multiplier = {"light":1.0,"Normal0":0.9,"Heavy":0.6}

def boot_sequence():
    print("Loading Main Menu...")
    for i in range(21):
        percent = i * 5
        bar = "█" * i + "-" * (20 - i)
        print(f"\r|{bar}| {percent}%", end="")
        time.sleep(0.1)
    print("\n\n--- ACCESS GRANTED ---\n")

def calculate_adjusted_speed(base_speed,time_mult,season_mult,traffic_mult):
    return base_speed * time_mult*season_mult*traffic_mult
def calculate_travel_time(distance, adjusted_speed, time_minutes=None):
    if adjusted_speed == 0:
        return 0,0
    time_hours = distance / adjusted_speed
    time_hours = time_hours * time_multiplier[time_hours]
    return time_hours, time_minutes 
    
def wave_menu():
    title = "MAIN MENU"
    options = ["1.Admin", "2.Estimate", "3.Exit"]

    # 1. Display the Title (Stationary)
    print(f"\n{'=' * 60}")
    print(f"{title:^60}")
    print(f"{'=' * 60}\n")

    # 2. Display the Waving Options
    for i, opt in enumerate(options):
        # The Logic:
        # Base offset of 5 spaces + a sine curve that moves up to 4 spaces
        indent_size = int(5 + 4 * math.sin(i * 1.5))

        indent = " " * indent_size
        print(f"{indent}◈ {opt}")
    print("")
    print(f"{'=' * 60}\n")


def main_menu():
    running = True
    has_booted = False

    while running:
        if not has_booted:
            boot_sequence()
            input("Press ANY to continue..")
            clear_screen()
            has_booted = True
        wave_menu()
        choice = input("Please choose(1-3)>>")
        if choice == '1':
            clear_screen()
            function1()
        elif choice == '2':
            clear_screen()
            print("Function2")
            input("Press Enter to continue...")
            clear_screen()
        elif choice == '3':
            clear_screen()
            print("Exiting...")
            running = False
        else:
            print("Unavailable choice.Please try again")


if __name__ == "__main__":
    main_menu()

