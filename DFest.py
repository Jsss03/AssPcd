#modeule  : DFest.py
#auther   : LING KS's students
#date     : 18-03-2026
#purpose  : perform estimation of time 
#import   : fileIO,menuDesign,datetime,random,time,DFweathers,holidays
#amendment:

import fileIO as IO
import menuDesign as menu
from datetime import datetime,timedelta
import random
import time
import DFweathers as wt
import holidays

def select_route():
    while True:
        menu.clear_screen()
        print("=" * 80)
        print("Applicable routes".center(80))
        print("=" * 80)
        print(f"{'No.':^4} | {'Departure':<25} | {'Destination':<25} | {'Distance (KM)'}")
        print("-" * 80)

        for i,route in enumerate(IO.location_matrix,start=1):
            print(f"{i:^4} | {route[0]:<25} | {route[1]:<25} | {route[2]}")
        print("=" * 80)
        choice=input("<B>ack\n\nPlease select route number>> ").upper()
        if choice =='B':
            return None
        try:
            route_idx=int(choice) -1
            if route_idx<0 or route_idx>= len(IO.location_matrix):
                print("Selection out of range! Please try again.")
                time.sleep(1)
                continue
            selected_route=IO.location_matrix[route_idx]
            return selected_route
        except (ValueError,IndexError):
            print("Invalid selection! Please try again.")
            time.sleep(1)
            continue

def select_transportation():
    while True:
        menu.clear_screen()
        print("=" * 70)
        print("Available transportation".center(70))
        print("=" * 70)
        print(f"{'No.':^4} | {'Transport types'}")
        print("-" * 70)

        for i,type in enumerate(IO.transportation,start=1):
            print(f"{i:^4} | {type[0]:<25}")
        print("=" * 70)
        choice=input("<B>ack\n\nPlease select transportation type >> ").upper()
        if choice =='B':
            return None
        try:
            idx=int(choice) -1
            if idx<0 or idx>= len(IO.transportation):
                print("Selection out of range! Please try again.")
                time.sleep(1)
                continue
            transportation_lst=IO.transportation[idx]
            transportation_type=transportation_lst[0]
            base_speed=float(transportation_lst[1])
            return transportation_type,base_speed
        except (ValueError,IndexError):
            print("Invalid selection! Please try again.")
            time.sleep(1)
            continue


def get_time_multiplier(timing):
    time_multiplier = {"Morning": 0.75,"Afternoon": 1.0, "Evening peak": 0.7, "Night": 1.15, "other":1.0}
    time_mult = time_multiplier.get(timing)
    return time_mult


def get_traffic_multiplier():
    now=datetime.now()
    seed_value=f"{now.date()}-{now.hour}-{now.minute//10}"
    random.seed(seed_value)
    conditions = {"Light": 1.2, "Normal": 1.0, "Heavy": 0.5}
    status=random.choice(list(conditions.keys()))
    traffic_mult = conditions[status]
    random.seed()
    return status,traffic_mult

def get_special_days_multiplier():
    py_holidays=holidays.MY()
    today=datetime.now()
    tomorrow=today + timedelta(days=1)
    is_holiday_eve=tomorrow in py_holidays
    is_holiday=today in py_holidays
    is_friday=today.weekday() == 4
    if is_friday and is_holiday_eve :
        return 0.5,"Friday and also holiday eve"
    elif is_friday and is_holiday :
        return 0.5,"Friday and also holiday"
    elif is_holiday_eve or is_holiday:
        return 0.8,"Holiday"
    elif is_friday:
        return 0.85,"Friday"
    else:
        return 1.0,"Normal day"
    
def get_season_multiplier(weather):
    weather_multiplier = {"Sunny": 1.0, "Cloudy":0.95, "Light Rain": 0.9, "Heavy Rain": 0.80}
    special_day_mult,special_day_status=get_special_days_multiplier()
    weather_mult= weather_multiplier.get(weather)
    season_mult = weather_mult * special_day_mult
    return season_mult,special_day_status,weather_mult

def analyse_timing():
    nowHH=datetime.now().hour
    time_map=[(7,11,"Morning"),(12,15,"Afternoon"),
              (16,20,"Evening peak"),(21,23,"Night"),(0,6,"Night")]
    for start,end,label in time_map:
        if start <= nowHH <= end:
            return label
    return "other"

def analyse_weather():
    weather=wt.get_weather_data()
    condition=weather["cond"]
    return condition

def calculate_adjusted_speed(trans_data):
    transportation_type,base_speed = trans_data
    timing=analyse_timing()
    time_mult = get_time_multiplier(timing)
    weather = analyse_weather()
    season_mult,special_day_status,weather_mult = get_season_multiplier(weather)
    status,traffic_mult = get_traffic_multiplier()
    menu.clear_screen()
    print("="*70)
    print("Travel Time Estimation".center(70))
    print("="*70)
    print(f"{'Transportation type':^25} : {transportation_type}")
    print(f"{'Time of day':^25} : {timing}")
    print(f"{'Weather':^25} : {weather}")
    if transportation_type not in ["Walking","Bicycle"]:
        print(f"{'Traffic condition':^25} : {status}")
        print(f"{'Season':^25} : {special_day_status}")
    if transportation_type == "Walking" or transportation_type =="Bicycle":
        adjusted_speed=base_speed * weather_mult

    else:
        adjusted_speed = base_speed * time_mult*season_mult*traffic_mult
    return adjusted_speed,weather

def cal_esTime(route_data,trans_data):
    
    distance=float(route_data[2])
    adjusted_speed,weather = calculate_adjusted_speed(trans_data)
    if adjusted_speed is None:
        return
    adjusted_speed=float(adjusted_speed)
    esTime=distance/adjusted_speed #getting value in hour unit
    departure_time=datetime.now()
    hours=int(esTime//1)
    minutes=esTime*60 %60
    travel_duration=timedelta(hours=hours,minutes=minutes)
    arrival_time=departure_time+travel_duration
    if minutes*100%100>=50:
        minutes=minutes//1 + 1
        minutes=int(minutes)
    else:
        minutes=int(minutes)
    print(f"{'Departure time':^25} : {departure_time.strftime("%I:%M %p")}")
    print(f"{'Estimated arrival time':^25} : {arrival_time.strftime("%I:%M %p")}")
    hh_text= hours>0 and f"{hours} hour(s) " or ""
    print(f"{'Estimated duration':^25} : {hh_text}{minutes} minute(s)")
    print("="*70)
    if weather in ["Light Rain","Heavy Rain"] and trans_data[0]in ["Walking","Bicycle"]:
        print(f"{'Please avoid walking or bicycling outdoor while raining!!!':^70}")
    else:
        print(f"{'Drive with care, arrive alive!!!':^70}")
    input("\nEnter any to continue.")
    IO.save_to_history(route_data)
    menu.clear_screen()
