#modeule  : fileIO.py
#auther   : LING KS's students
#date     : 16-03-2026
#purpose  : perform file input/output 
#import   : os(system),time,menuDesign
#amendment:

import os
import time
import menuDesign as menu
import DFest as est

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR,"location.txt")
HISTORY_FILE=os.path.join(BASE_DIR,"history.txt")
TRANSPORTATION_FILE = os.path.join(BASE_DIR, "transportation.txt")

default_routes = [["KLCC", "Bangsar Shopping mall", "13"],
                  ["UTAR-SL", "Mid Valley", "21.2"], ["UTAR-SL", "Sunway Pyramid", "30.6"], 
                  ["TARUMT", "Pavilion", "12.3"], ["UTAR-SL", "Sunway Velocity", "13.4"]]
default_transportation = ["Car|60", "Motorcycle|80", "Bicycle|15", "Walking|5"]

def sync_transportation():
    if not os.path.exists(TRANSPORTATION_FILE):
        with open(TRANSPORTATION_FILE, "w") as f:
            for v in default_transportation:
                f.write(v + "\n")
    
    elif os.stat(TRANSPORTATION_FILE).st_size == 0:
        with open(TRANSPORTATION_FILE, "a") as f:
            for v in default_transportation:
                f.write(v + "\n")

def load_transportation():
    vehicle_list = []
    if os.path.exists(TRANSPORTATION_FILE):
        with open(TRANSPORTATION_FILE, "r") as f:
            for line in f:
                if "|" in line:
                    name, speed = line.strip().split("|")
                    vehicle_list.append([name, speed])
    return vehicle_list

def save_transportation(transportation_list):
    with open(TRANSPORTATION_FILE, "w") as f:
        for v in transportation_list:
            f.write(f"{v[0]}|{v[1]}\n")

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
    location_matrix.append([loc_from,loc_to,loc_distance])
    print("\nNew route added succesfully.")
    time.sleep(1)

def remove_location():
        global location_matrix
        if not location_matrix:
            print("No routes to delete.")
            return

        print("--- REMOVE ROUTE ---")
        for i, row in enumerate(location_matrix):
            print(f"{i+1}. {row[0]} to {row[1]}")

        choice = input("\nSelect number to delete (<Q>uit): ")

        if choice.upper() == 'Q':
            return

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(location_matrix):
                # Remove from the list
                removed = location_matrix.pop(idx)
                # OVERWRITE the file with the new list (using "w")
                with open(FILENAME, "w") as f:
                    for row in location_matrix:
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

def manage_vehicles_logic():
    while True:
        menu.clear_screen()
        print("="*70)
        print("TRANSPORT MANAGEMENT".center(70))
        print("="*70)
        print(f"{'No.':^4} | {'Transport Types':<35} | {'Speed (km/h)'}")
        print("-"*70)
        for i, v in enumerate(transportation, 1):
            print(f"{i:^4} | {v[0]:<35} | {v[1]}")
        
        print("\n<A>dd   <E>dit   <D>elete   <B>ack")
        opt = input("\nPlease select next instruction >> ").upper()

        if opt == "A":
            step = 1
            name = ""
            speed = ""
            
            while step <= 2:
                menu.clear_screen()
                print("ADD NEW TRANSPORTATION".center(70))
                print(f"{'No.':^4} | {'Transport Types':<35} | {'Speed (km/h)'}")
                print("-"*70)
                for i, v in enumerate(transportation, 1):
                    print(f"{i:^4} | {v[0]:<35} | {v[1]}")
                print("\n<B>ack")
                if step == 1:
                    name = input("\nEnter new transportation>> ").capitalize()
                    if name.upper() == 'B': break
                    if any(v[0] == name for v in transportation):
                        print(f"{name} already exists!")
                        time.sleep(1.5)
                        continue
                    step = 2
                
                elif step == 2:
                    print(f"New transportation: {name}")
                    speed = input("Enter Average Speed (km/h)>> ")
                    if speed.upper() == 'B':
                        step = 1
                        continue
                    try:
                        speed=float(speed)
                        print(f"\nNew transportation: {name}\nSpeed: {speed} km/h")
                        slc=input("\nPlease <C>onfirm or enter ANY to back >> ").upper()
                        if slc=="C":
                            transportation.append([name, speed])
                            save_transportation(transportation)
                            print("\n[+] Database Updated!")
                            time.sleep(1)
                            step = 3
                        else:
                            step=2
                    except:
                        print("Enter digit only!")
                        time.sleep(1.5)
                        step=2
        elif opt == "E":
            while True:
                menu.clear_screen()
                print("EDIT TRANSPORTATION".center(70))
                print(f"{'No.':^4} | {'Transport Types':<35} | {'Speed (km/h)'}")
                print("-"*70)
                for i, v in enumerate(transportation, 1):
                    print(f"{i:^4} | {v[0]:<35} | {v[1]}")
                idx_in = input("\n<B>ack\n\nSelect No. to edit speed>> ")
                if idx_in.upper() == 'B': break        
                if idx_in.isdigit() and 0 < int(idx_in) <= len(transportation):
                    idx = int(idx_in) - 1
                    while True:
                        menu.clear_screen()
                        print(f"--- UPDATING {transportation[idx][0].upper()} ---")
                        new_speed = input(f"Enter New Speed (km/h)>> ")
                        try:
                            new_speed=float(new_speed)
                            slc=input("\nPlease <C>onfirm or enter ANY to back >> ").upper()
                            if slc=="C":
                                transportation[idx][1] = new_speed
                                save_transportation(transportation)
                                print("\nSpeed Updated successfully!")
                                time.sleep(1)
                                break
                            else:
                                continue
                        except:
                            print("Enter digit only!")
                            time.sleep(1.5)

        elif opt == "D":
            menu.clear_screen()
            print("DELETE TRANSPORTATION".center(70))
            print(f"{'No.':^4} | {'Transport Types':<35} | {'Speed (km/h)'}")
            print("-"*70)
            for i, v in enumerate(transportation, 1):
                print(f"{i:^4} | {v[0]:<35} | {v[1]}")
            idx_in = input("\n<B>ack\n\nSelect No. to delete>> ").upper()
            if idx_in=="B":
                continue
            if idx_in.isdigit() and 0 < int(idx_in) <= len(transportation):
                transportation.pop(int(idx_in) - 1)
                save_transportation(transportation)
                print("Transportation deleted successfully!")
                time.sleep(1)

        elif opt == "B":
            break

        
def save_to_history(route_data):
    if route_data is None:
        return None
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{timestamp}|{route_data[0]}|{route_data[1]}|{route_data[2]}\n")

def view_history():
    menu.clear_screen()
    print("="*80)
    print("TRAVELLING ESTIMATION HISTORY".center(80))
    print("="*80)
    if not os.path.exists(HISTORY_FILE):
        print("No file history found.")
        time.sleep(2)
        return
    print(f"{'Date/Time':<25} | {'Departure':<25} | {'Destination':<25}")
    print("-" * 80)
    try:
        with open(HISTORY_FILE, "r") as f:
            for line in f:
                # Split the line by the '|' symbol we used to save it
                data = line.strip().split("|")
                if len(data) == 4:
                    ts, f_loc, t_loc, dist = data
                    # Print it out formatted into columns
                    print(f"{ts:<25} | {f_loc:<25} | {t_loc:<25}")
    except Exception as e:
        print(f"Error reading history: {e}")
    input("\nEnter ANY to return...")
  
  
sync_defaults()
sync_transportation()
location_matrix = load_matrix()
transportation = load_transportation()
