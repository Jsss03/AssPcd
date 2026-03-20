#modeule  : DFAdmin.py
#auther   : LING KS's students
#date     : 18-03-2026
#purpose  : perform admin management
#import   : fileIO,menuDesign
#amendment:

import fileIO as IO
import menuDesign as menu

def admin_management():
    """GROUP A: Logic for managing locations (CRUD) """
    while True:
        menu.clear_screen()
        print("--- ADMIN MANAGEMENT ---")
        print("1. View Current Routes")
        print("2. View history")
        print("3. Return to Main Menu")

        choice = input("\nPlease choose 1-3 >> ")
        while choice == '1':
            menu.clear_screen()
            matrix = IO.load_matrix()
            print("=" * 70)
            print("CURRENT ROUTES".center(70))
            print("=" * 70)
            print(f"{'Departure':<25} | {'Destination':<25} | {'Distance (KM)'}")
            print("-" * 70)
            for row in matrix:
                print(f"{row[0]:<25} | {row[1]:<25} | {row[2]}")
            opt=input("\n<A>dd     <D>elete     <B>ack\n\nPlease enter next insturction>> ").upper()
            if opt=="A":
                menu.clear_screen()
                print("---ADD LOCATION---")
                print("\n<Q>uit     <B>ack")
                IO.add_new_place()
            elif opt=="D":
                menu.clear_screen()
                IO.remove_location()
            elif opt=="B":
                menu.clear_screen()
                break
        if choice == '2':
            IO.view_history()
        if choice == '3':
            menu.clear_screen()
            break
    
