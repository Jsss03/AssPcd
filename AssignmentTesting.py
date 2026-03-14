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
    

def clear_screen():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def add_new_place():
    step=1
    loc_from=""
    loc_to=""
    distance=""

    while step<=3:
        clear_screen()
        print("\n"+'='*20)
        print("ADMIN: ADD PLACE")
        print("="*20)
        print("(q:Quit | b: Back to previous)")
        print("="*20)

        if step==1:
            loc_from=input("Enter 'From' Location: ")
            if loc_from.lower()=='q' or loc_from.lower()=='b': return
            step=2

        elif step==2:
            print(f"From: {loc_from}")
            loc_to=input("Enter 'To' Location: ")
            if loc_to.lower()=='q':return
            if loc_to.lower()=='b':
                step=1
                continue
            step=3

        elif step==3:
            print(f"From: {loc_from}")
            print(f"To: {loc_to}")
            loc_distance=input("Enter Distance (km): ")
            if loc_distance.lower()=='q':return
            if loc_distance.lower()=='b':
                step=2
                continue
            step=4

    new_entry=f"{loc_from}|{loc_to}|{loc_distance}\n"
    with open(FILENAME,"a")as f:
        f.write(new_entry)
    print("\n--- Data succesfully saved to "+ FILENAME+"---")
    
def admin_management():
    """GROUP A: Logic for managing locations (CRUD) """
    while True:
        clear_screen()
        print("--- ADMIN MANAGEMENT ---")
        print("1. View Current Routes")
        print("2. Add New Places")
        print("3. Return to Main Menu")

        choice = input("\nPlease choose 1-3 >> ")
        if choice == '1':
            matrix = load_matrix()
            print(f"\n{'Start':<15} | {'Destination':<25} | {'Dist (KM)'}")
            print("-" * 55)
            for row in matrix:
                print(f"{row[0]:<15} | {row[1]:<25} | {row[2]}")
            input("\nPress Enter to continue...")
        elif choice == '2':
            add_new_place()
 
        elif choice == '3':
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
    options = ["1.Admin", "2.Estimate", "3.Help Centre","4.Exit"]
    
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

def get_time_multiplier(timing):
    time_multiplier = {"morning":0.75,"afternoon":1.0,"evening":0.7,"night":1.15}
    time_mult=time_multiplier.get(timing)
    return time_mult

def get_season_multiplier(season):
    season_multiplier ={"normal":1.0,"rainy":0.85,"festive_holiday":0.80}
    season_mult=season_multiplier.get(season)
    return season_mult

def get_traffic_multiplier(traffic):
    traffic_multiplier = {"light":1.0,"normal":0.9,"Heavy":0.6}
    traffic_mult=traffic_multiplier.get(traffic)
    return traffic_mult

def get_base_speed(transport):
    transport_modes = {"walking":5,"bicycle":15,"car":60,"bus":40}
    base_speed=transport_modes.get(transport)
    return base_speed
    
def calculate_adjusted_speed():
    transport=input("Enter transport>>")
    base_speed=get_base_speed(transport)
    timing=input("Enter timing>>")
    time_mult=get_time_multiplier(timing)
    season=input("Enter season>>")
    season_mult=get_season_multiplier(season)
    traffic=input("Enter traffic>>")
    traffic_mult=get_traffic_multiplier(traffic)
    adjusted_speed= base_speed * time_mult*season_mult*traffic_mult
    return adjusted_speed
    
def ai_customer_service():
    brain = {"price": "Our travel costs are calculated based on distance. Walking is free!",\
        "weather": "Rain increases travel time by 50% for safety.",\
        "time": "Travel time = (Distance / Speed) multiplied by traffic and weather factors.",\
        "cost": "Travel cost depends on your transport mode. We aim to keep it affordable for students!",\
        "rain": "Our system detects rainy weather and adjusts the estimated time automatically.",\
        "traffic": "Traffic is generated randomly to simulate real-world delays.",\
        "hello": "Hi there! I am your AI assistant. How can I help you?",\
        "hi": "Hello! Ask me anything about price, weather, or traffic.",\
        "location": "You can add custom locations in the Admin Management menu!",\
        "fast": "The Car is the fastest mode, but 'Evening Peak' traffic can slow you down significantly.",\
        "student": "Welcome UTAR student! Good luck with your assignment!"}

    print("\n" + "="*50)
    print("        🤖 AI TRAVEL ASSISTANT")
    print("    (Type 'b' to go BACK to Main Menu)")
    print("="*50)

    while True:
        user_query = input("\n[AI Chat] Ask me anything >> ").lower()

        # GO BACK LOGIC
        if "bye" in user_query or "thank you" in user_query or "thanks" in user_query or "tq" in user_query or "ok" in user_query:
            print("\n[AI]: It was a pleasure helping you. Safe travels!")
            break
        if user_query == 'b' or user_query == 'back' or user_query == 'exit':
            print("\n[AI]: Returning to Main Menu...")
            time.sleep(1)
            break # This exits the while loop and goes back to your menu

        found_match = False
        for keyword in brain:
            if keyword in user_query:
                print(f"\n[AI]: {brain[keyword]}")
                found_match = True
                break 

        if not found_match:
            print("\n[AI]: I'm not sure about that. Try asking about 'Price', 'Weather', 'Traffic', or 'Time'..")
            
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
        choice=input("Please choose(1-4)>>")
        if choice=='1':
            clear_screen()
            admin_management()
        elif choice=='2':
            clear_screen()
            print("Function2")
            input("Press Enter to continue...")
            clear_screen()
        elif choice=='3':
            clear_screen()
            ai_customer_service()
        elif choice=='4':
            clear_screen()
            print("Exiting...")
            running=False
        else:
            print("Unavailable choice.Please try again")

if __name__=="__main__":
    main_menu()
