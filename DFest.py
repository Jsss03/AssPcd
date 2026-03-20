#modeule  : DFest.py
#auther   : LING KS's students
#date     : 18-03-2026
#purpose  : perform estimation of time 
#import   : os(system)
#amendment:

import fileIO as IO
import menuDesign as menu
from datetime import datetime
import random
import time

def select_route():
    print("=" * 80)
    print("Applicable routes".center(80))
    print("=" * 80)
    print(f"{'No.':^4} | {'Departure':<25} | {'Destination':<25} | {'Distance (KM)'}")
    print("-" * 80)

    for i,route in enumerate(IO.location_matrix,start=1):
        print(f"{i:^4} | {route[0]:<25} | {route[1]:<25} | {route[2]}")

    try:
        choice=input("\n<B>ack\nPlease select route number>> ").upper()
        if choice =='B':
            return None
        route_idx=int(choice) -1
        selected_route=IO.location_matrix[route_idx]
        distance=float(selected_route[2])
        return distance
    except (ValueError,IndexError):
        print("Invalid selection! Please try again.")
        time.sleep(3)
        return None


def get_time_multiplier(timing):
    time_multiplier = {"morning": 0.75,"afternoon": 1.0, "evening peak": 0.7, "night": 1.15, "other":2.0}
    time_mult = time_multiplier.get(timing)
    return time_mult


def get_season_multiplier(season):
    season_multiplier = {"normal": 1.0, "rainy": 0.85, "festive_holiday": 0.80}
    season_mult = season_multiplier.get(season)
    return season_mult


def get_traffic_multiplier():
    now=datetime.now()
    seed_value=f"{now.date()}-{now.hour}-{now.minute//10}"
    random.seed(seed_value)
    conditions = {"light": 1.2, "normal": 1.0, "heavy": 0.5}
    status=random.choice(list(conditions.keys()))
    traffic_mult = conditions[status]
    random.seed()
    return status,traffic_mult


def get_base_speed(transport):
    transport_modes = {"walking": 5, "bicycle": 15, "car": 60, "bus": 40}
    base_speed = transport_modes.get(transport)
    return base_speed

def analyse_timing():
    nowHH=datetime.now().hour
    time_map=[(7,9,"morning"),(12,14,"afternoon"),
              (17,20,"evening peak"),(21,23,"night"),(0,6,"night")]
    for start,end,label in time_map:
        if start <= nowHH < end:
            return label
    return "other"


def calculate_adjusted_speed():
    transport = input("Enter transport>>")
    base_speed = get_base_speed(transport)
    timing=analyse_timing()
    time_mult = get_time_multiplier(timing)
    season = input("Enter season>>")
    season_mult = get_season_multiplier(season)
    status,traffic_mult = get_traffic_multiplier()
    print(f"Transport type: {transport} \nTime of day : {timing} \nTraffic condition : {status}")
    if transport == "walking" or transport=="bicycle":
        adjusted_speed=base_speed
    else:
        adjusted_speed = base_speed * time_mult*season_mult*traffic_mult
    return adjusted_speed

def cal_esTime():
    distance=select_route()
    if distance==None:
        menu.clear_screen()
        return None
    menu.clear_screen()
    adjusted_speed = float(calculate_adjusted_speed())
    esTime=distance/adjusted_speed
    hour=int(esTime//1)
    minutes=esTime*60 %60
    if minutes*100%100>=50:
        minutes=minutes//1 + 1
        minutes=int(minutes)
    else:
        minutes=int(minutes)
    if hour==0:
        print(f"Estimated time : {minutes}minute(s)")
    else:
        print(f"Estimated time : {hour}hour(s) {minutes}minute(s)")
    input("Press any to continue.")
    menu.clear_screen()
