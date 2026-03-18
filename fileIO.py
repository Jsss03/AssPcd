#modeule  : fileIO.py
#auther   : LING KS's students
#date     : 16-03-2026
#purpose  : perform file input/output 
#import   : os(system),time,menuDesign
#amendment:

import os
import time
import menuDesign as menu

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR,"location.txt")
default_routes = [["KLCC", "Bangsar Shopping mall", "13"],
                  ["UTAR-SL", "Mid Valley", "21.2"], ["UTAR-SL", "Sunway Pyramid", "30.6"], ["TARUMT", "Pavilion", "12.3"], ["UTAR-SL", "Sunway Velocity", "13.4"]]
    
def sync_defaults():
    existing_lines = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            existing_lines = [line.strip() for line in f if line.strip()]
    with open(FILENAME, "a") as f:
        for route in default_routes:
            route_str = "|".join(route)
            if route_str not in existing_lines:
                f.write(route_str + "\n")


def load_matrix():
    matrix = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r")as f:
            for line in f:
                if line.strip():
                    matrix.append(line.strip().split("|"))
    return matrix


sync_defaults()
location_matirx = load_matrix()

def add_new_place():
    step = 1
    loc_from = ""
    loc_to = ""
    distance = ""

    while step <= 4:
        menu.clear_screen()
        print("---ADD LOCATION---")
        print("\n<Q>uit     <B>ack")
        if step == 1:
            loc_from = input("\nEnter 'From' Location: ")
            if loc_from.upper() == 'B' or loc_from.upper() == 'Q':
                return
            step = 2

        elif step == 2:
            print(f"From:{loc_from}")
            loc_to = input("Enter 'To' Location: ")
            if loc_to.upper() == 'Q':
                return
            if loc_to.upper() == 'B':
                step = 1
                continue
            matrix=load_matrix()
            is_duplicate = False
            for row in matrix:
                if row[0].lower()==loc_from.lower() and row[1].lower()==loc_to.lower():
                    is_duplicate= True
                    break
            if is_duplicate:
                print(f"!!Error: The route {loc_from} to {loc_to} already exists!")
                time.sleep(2)
                return
            step = 3

        elif step == 3:
            print(f"From:{loc_from}")
            print(f"To:{loc_to}")
            loc_distance = input("Enter Distance (km): ")
            if loc_distance.upper() == 'Q':
                return
            if loc_distance.upper() == 'B':
                step = 2
                continue
            try:
                float(loc_distance)
                step=4
            except:
                input("Opps Error!Please Try Again!")
        elif step==4:
            menu.clear_screen()
            print("--- Route Confirmation ---")
            print(f"From     : {loc_from}")
            print(f"To       : {loc_to}")
            print(f"Distance : {loc_distance} km")
            confirmation=input("\n<C>onfirm     <B>ack     <Q>uit\n").upper()
            if confirmation=="C":
                step=5
            elif confirmation=="B":
                step=3
            elif confirmation=="Q":
                return
            else:
                print("Invalid.Plaese try again!")
                step=4

    new_entry = f"{loc_from}|{loc_to}|{loc_distance}\n"
    with open(FILENAME, "a")as f:
        f.write(new_entry)
    print("\nNew route added succesfully.")
    time.sleep(1)

def remove_location():
        matrix = load_matrix()

        if not matrix:
            print("No routes to delete.")
            return

        print("--- REMOVE ROUTE ---")
        for i, row in enumerate(matrix):
            print(f"{i+1}. {row[0]} to {row[1]}")

        choice = input("\nSelect number to delete (<Q>uit): ")

        if choice.upper() == 'Q':
            return

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(matrix):
                # Remove from the list
                removed = matrix.pop(idx)
                # OVERWRITE the file with the new list (using "w")
                with open(FILENAME, "w") as f:
                    for row in matrix:
                        f.write("|".join(row) + "\n")
                    print(f"Successfully deleted: {removed[0]} to {removed[1]}")
            else:
                print("Invalid number.")
        except:
            print("Please enter a valid number.")

        time.sleep(1)
    
def get_distance_from_file(FILENAME):
    search_from = input("Enter starting location>> ")
    search_to = input("Enter destination>> ")
    found = False

    try:
        with open(FILENAME, "r")as f:
            for line in f:
                data = line.strip().split("|")
                if len(data) == 3:
                    loc_from = data[0].strip()
                    loc_to = data[1].strip()
                    distance = data[2].strip()
                    if loc_from.lower() == search_from.lower() and loc_to.lower() == search_to.lower():
                        print(f"Distance from {loc_from} to {loc_to} : {distance} km")
                        return float(distance)
            print("Sorry! Location not found!")
            return None

    except FileNotFoundError:
        print("Error.File not found!")
        return None
