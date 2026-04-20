#modeule  : AIcs.py
#auther   : Group #
#date     : 18-03-2026
#purpose  : perform ai customer service
#import   : time, menuDesign
#amendment:

import time
import menuDesign as menu

def ai_customer_service():
    brain = {
        "history": "You can view your past travel estimations by selecting View History in the Admin menu.",
        "hi": "Hi there! I am your AI assistant. How can I help you?",
        "hello": "Hello! Ask me anything about route, fastest way, or traffic.",
        "eta": "Your ETA is calculated using weather, speed, and time-of-day multipliers.",
        "traffic": "I adjust your speed based on Morning, Evening peak, and Night traffic patterns.",
        "hazard": "If it's 'Heavy Rain', I'll warn you to drive with extra care or avoid cycling.",
        "route": "Select 'Estimate travel time' to pick a route and see your arrival time.",
        "report": "You can add or edit custom locations in the Admin Management menu!",
        "fastest": "Travel time is calculated using Distance and Adjusted Speed based on current conditions.",
        "alerts": "Check the Main Menu dashboard for live temperature and weather updates!",
        "holiday": "I check for public holidays and holiday eves which can slow down traffic.",
        "about you": "I'm created by UTAR's Students-Chin Jia Wei,Chen Hui Yang,Goh Jin Seng,How Han Bin, Law Wei Jun and Lee Yu Ze!"}

    print("\n" + "="*50)
    print("        🤖 AI TRAVEL ASSISTANT")
    print("    (Type 'b' to go BACK to Main Menu)")
    print("="*50)
    print("\n[AI]:Hi there! I am your AI assistant. How can I help you?")
    loop=True
    while loop:
        user_query = input("\n[YOU] >> ").lower()

        # GO BACK LOGIC
        if user_query in ['bye','thank you','thanks','tq','ok']:
            print("\n[AI]: It was a pleasure helping you. Safe travels!")
            time.sleep(1.5)
            menu.clear_screen()
            loop=False
        if user_query in ['b','back','exit']:
            print("\n[AI]: Returning to Main Menu...")
            time.sleep(0.5)
            menu.clear_screen()
            loop=False  # This exits the while loop and goes back to your menu

        found_match = False
        for keyword in brain:
            if keyword in user_query:
                print(f"\n[AI]: {brain[keyword]}")
                found_match = True
                break

        if not found_match:
            print(
                "\n[AI]: I'm not sure about that. Try asking about 'Price', 'Weather', 'Traffic', or 'Time'..")
