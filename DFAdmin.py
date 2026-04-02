#modeule  : DFAdmin.py
#auther   : LING KS's students
#date     : 18-03-2026
#purpose  : perform admin management
#import   : fileIO,menuDesign,time
#amendment:

import fileIO as IO
import menuDesign as menu
import time

def admin_management():
    """GROUP A: Logic for managing locations (CRUD) """
    while True:
        menu.clear_screen()
        print("="*70)
        print("ADMIN MANAGEMENT".center(70))
        print("="*70)
        print("1. View Current Routes")
        print("2. View Transportation")
        print("3. View History")
        print("4. Return to Main Menu")
        print("="*70)

        choice = input("\nPlease enter next instruction (1-4)>> ")
        if choice == '1':
            while True:
                menu.clear_screen()
                matrix = IO.load_matrix()
                print("=" * 70)
                print("CURRENT ROUTES".center(70))
                print("=" * 70)
                print(f"{'Departure':<25} | {'Destination':<25} | {'Distance (KM)'}")
                print("-" * 70)
                for row in matrix:
                    print(f"{row[0]:<25} | {row[1]:<25} | {row[2]}")
                print("="*70)
                opt=input("<A>dd     <E>dit     <D>elete     <B>ack\n\nPlease enter next insturction>> ").upper()
                if opt=="A":
                    menu.clear_screen()
                    print("---ADD LOCATION---")
                    print("\n<Q>uit     <B>ack")
                    IO.add_new_place()
                elif opt=="E":
                    menu.clear_screen()
                    IO.edit_location()
                elif opt=="D":
                    menu.clear_screen()
                    IO.remove_location()
                elif opt=="B":
                    menu.clear_screen()
                    break
                else:
                    print("Invalid choice! Please try again.")
                    time.sleep(1)
                    continue
        elif choice== '2':
            IO.manage_vehicles_logic()
        elif choice == '3':
            IO.view_history()
        elif choice == '4':
            menu.clear_screen()
            break
        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)
            continue
    
