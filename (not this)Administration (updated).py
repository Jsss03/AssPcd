#module   : Administration.py
#author   : LING KS's students
#date     : 27-03-2026
#purpose  : act as main
#import   : menuDesign, fileIO, DFAdmin, AIcs, DFest, DFweathers
#amendment: added login portal (Admin / Guest) before boot sequence

import menuDesign as menu
import fileIO as IO
import DFAdmin as Admin
import AIcs as cs
import DFest as est
import DFweathers as wt

# Self-defined admin password
ADMIN_PASSWORD = "1234"

def login():
    while True:                                    
        menu.clear_screen()
        print("=" * 70)
        print("WELCOME TO THE SYSTEM".center(70))
        print("=" * 70)
        print()
        print("  1. Log in as Admin")
        print("  2. Log in as Guest")
        print("  3. Quit")
        print()
        choice = input("Enter choice: ").strip()

        if choice == "1":                          
            # Admin: require password
            password = input("Enter Admin Password: ").strip()

            if password == ADMIN_PASSWORD:        
                print("\nAdmin login successful!")
                # FIX: Return the role to the main function
                return "admin"
            else:
                print("\nInvalid password. Returning to login...\n")
                import time
                time.sleep(1.5)

        elif choice == "2":
            # Guest: proceed to main menu
            return "guest"

        elif choice == "3":
            menu.clear_screen()
            print("Goodbye!")
            exit()

        else:
            print("\nInvalid choice. Try again.\n")
            import time
            time.sleep(1)

def main():
    
    # Fetch weather once at startup
    print("Syncing with weather satellites...")
    weather_storage = wt.get_weather_data("Cheras")

    # FIX: Capture the role returned by the login function
    role = login()

    running      = True
    has_booted   = False

    while running:                                 
        if not has_booted:
            menu.boot_sequence()
            input("Press ANY to continue..")
            has_booted = True
            menu.clear_screen()

        menu.main_menu(weather_storage, role)      # pass role so guest sees 3 options
        if role == "admin":
            choice = input("Please choose(1-4)>>")
        else:
            choice = input("Please choose(1-3)>>")

        if role == "admin":
            # Admin: 4 options
            if choice == '1':
                menu.clear_screen()
                Admin.admin_management()
            elif choice == '2':
                menu.clear_screen()
                route_data = est.select_route()
                trans_data = est.select_transportation()
                if route_data is None:
                    menu.clear_screen()
                    continue
                if trans_data is None:
                    menu.clear_screen()
                    continue
                est.cal_esTime(route_data, trans_data)
            elif choice == '3':
                menu.clear_screen()
                cs.ai_customer_service()
            elif choice == '4':
                menu.clear_screen()
                print("Exiting system...")
                running = False
            else:
                menu.clear_screen()
                input("Invalid choice.\nPress Enter to try again.")

        else:
            # Guest: 3 options (no Admin Management) 
            if choice == '1':
                menu.clear_screen()
                route_data = est.select_route()
                trans_data = est.select_transportation()
                if route_data is None:
                    menu.clear_screen()
                    continue
                if trans_data is None:
                    menu.clear_screen()
                    continue
                est.cal_esTime(route_data, trans_data)
            elif choice == '2':
                menu.clear_screen()
                cs.ai_customer_service()
            elif choice == '3':
                menu.clear_screen()
                print("Exiting system...")
                running = False
            else:
                menu.clear_screen()
                input("Invalid choice.\nPress Enter to try again.")


if __name__ == "__main__":
    main()
