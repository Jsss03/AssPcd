#modeule  : Main.py
#auther   : LING KS's students
#date     : 18-03-2026
#purpose  : act as main 
#import   : menuDesign,fileIO,DFAdmin,AIcs,DFest,DFweathers
#amendment:

import menuDesign as menu
import fileIO as IO
import DFAdmin as Admin
import AIcs as cs
import DFest as est
import DFweathers as wt

def main():
    role=IO.login()
    running = True
    has_booted = False
    print("Syncing with weather satellites...")
    weather_storage=wt.get_weather_data("Cheras")

    while running:
        if not has_booted:
            menu.boot_sequence()
            input("Press ANY to continue..")
            has_booted = True
            menu.clear_screen()
        menu.main_menu(weather_storage,role)
        if role == "admin":
            choice = input("Please enter next instruction (1-4)>> ")
        else:
            choice = input("Please enter next instruction (1-3)>> ")

        if role == "admin":
            # Admin: 4 options
            if choice == '1':
                menu.clear_screen()
                Admin.admin_management()
            elif choice == '2':
                step=1
                loop=True
                route_data=None
                trans_data=None
                while loop:
                    menu.clear_screen()
                    if step==1:
                        route_data = est.select_route()
                        if route_data is None:
                            menu.clear_screen()
                            loop=False
                        else:
                            step=2
                        
                    elif step==2:
                        trans_data = est.select_transportation()
                        if trans_data is None:
                            step=1
                            route_data=None
                        else:
                            est.cal_esTime(route_data, trans_data)
                            loop=False
            elif choice == '3':
                menu.clear_screen()
                cs.ai_customer_service()
            elif choice == '4':
                menu.clear_screen()
                print("Exiting system...")
                running = False
            else:
                input("Invalid choice.\nPress Enter to try again.")
                menu.clear_screen()

        else:
            # Guest: 3 options (no Admin Management) 
            if choice == '1':
                step=1
                loop=True
                route_data=None
                trans_data=None
                while loop:
                    menu.clear_screen()
                    if step==1:
                        route_data = est.select_route()
                        if route_data is None:
                            menu.clear_screen()
                            loop=False
                        else:
                            step=2
                        
                    elif step==2:
                        trans_data = est.select_transportation()
                        if trans_data is None:
                            step=1
                            route_data=None
                        else:
                            est.cal_esTime(route_data, trans_data)
                            loop=False

            elif choice == '2':
                menu.clear_screen()
                cs.ai_customer_service()
            elif choice == '3':
                menu.clear_screen()
                print("Exiting system...")
                running = False
            else:
                input("Invalid choice.\nPress Enter to try again.")
                menu.clear_screen()


if __name__ == "__main__":
    main()
