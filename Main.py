#modeule  : Main.py
#auther   : LING KS's students
#date     : 18-03-2026
#purpose  : act as main 
#import   : menuDesign,fileIO,DFAdmin,AIcs,DFest
#amendment:

import menuDesign as menu
import fileIO as IO
import DFAdmin as Admin
import AIcs as cs
import DFest as est
import DFweathers as wt

def main():
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
        menu.wave_menu(weather_storage)
        choice = input("Please choose(1-4)>>")
        if choice == '1':
            menu.clear_screen()
            Admin.admin_management()
        elif choice == '2':
            menu.clear_screen()
            est.cal_esTime()
            input("Press any to continue.")
            menu.clear_screen()
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


if __name__ == "__main__":
    main()
