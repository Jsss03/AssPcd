#modeule  : AIcs.py
#auther   : Group 3
#date     : 18-03-2026
#purpose  : perform ai customer service
#import   : time, menuDesign
#amendment:

import time
import menuDesign as menu

def ai_customer_service():
    brain = {"price": "Our travel costs are calculated based on distance. Walking is free!",
             "weather": "Rain increases travel time by 50% for safety.",
             "time": "Travel time = (Distance / Speed) multiplied by traffic and weather factors.",
             "rain": "Our system detects rainy weather and adjusts the estimated time automatically.",
             "traffic": "Traffic is generated based on time .",
             "hi": "Hi there! I am your AI assistant. How can I help you?",
             "hello": "Hello! Ask me anything about price, weather, or traffic.",
             "location": "You can add custom locations in the Admin Management menu!",
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
        if "bye" in user_query or "thank you" in user_query or "thanks" in user_query or "tq" in user_query or "ok" in user_query:
            print("\n[AI]: It was a pleasure helpi#modeule  : AIcs.py
#auther   : Group 3
#date     : 18-03-2026
#purpose  : perform ai customer service
#import   : time, menuDesign
#amendment:

import time
import menuDesign as menu

def ai_customer_service():
    brain = {"price": "Our travel costs are calculated based on distance. Walking is free!",
             "weather": "Rain increases travel time by 50% for safety.",
             "time": "Travel time = (Distance / Speed) multiplied by traffic and weather factors.",
             "rain": "Our system detects rainy weather and adjusts the estimated time automatically.",
             "traffic": "Traffic is generated based on time .",
             "hi": "Hi there! I am your AI assistant. How can I help you?",
             "hello": "Hello! Ask me anything about price, weather, or traffic.",
             "location": "You can add custom locations in the Admin Management menu!",
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
        if "bye" in user_query or "thank you" in user_query or "thanks" in user_query or "tq" in user_query or "ok" in user_query:
            print("\n[AI]: It was a pleasure helping you. Safe travels!")
            time.sleep(1.5)
            menu.clear_screen()
            loop=False
        if user_query == 'b' or user_query == 'back' or user_query == 'exit':
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
                "\n[AI]: I'm not sure about that. Try asking about 'Price', 'Weather', 'Traffic', or 'Time'..")ng you. Safe travels!")
            time.sleep(1.5)
            menu.clear_screen()
            loop=False
        if user_query == 'b' or user_query == 'back' or user_query == 'exit':
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
