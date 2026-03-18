#modeule  : DFest.py
#auther   : LING KS's students
#date     : 18-03-2026
#purpose  : perform estimation of time 
#import   : os(system)
#amendment:

import fileIO as IO

def get_time_multiplier(timing):
    time_multiplier = {"morning": 0.85,"afternoon": 1.0, "evening": 0.7, "night": 1.15}
    time_mult = time_multiplier.get(timing)
    return time_mult


def get_season_multiplier(season):
    season_multiplier = {"normal": 1.0, "rainy": 0.85, "festive_holiday": 0.80}
    season_mult = season_multiplier.get(season)
    return season_mult


def get_traffic_multiplier(traffic):
    traffic_multiplier = {"light": 1.0, "normal": 0.9, "heavy": 0.6}
    traffic_mult = traffic_multiplier.get(traffic)
    return traffic_mult


def get_base_speed(transport):
    transport_modes = {"walking": 5, "bicycle": 15, "car": 60, "bus": 40}
    base_speed = transport_modes.get(transport)
    return base_speed


def calculate_adjusted_speed():
    transport = input("Enter transport>>")
    base_speed = get_base_speed(transport)
    timing = input("Enter timing>>")
    time_mult = get_time_multiplier(timing)
    season = input("Enter season>>")
    season_mult = get_season_multiplier(season)
    traffic = input("Enter traffic>>")
    traffic_mult = get_traffic_multiplier(traffic)
    if transport == "walking" or transport=="bicycle":
        adjusted_speed=base_speed
    else:
        adjusted_speed = base_speed * time_mult*season_mult*traffic_mult
    return adjusted_speed

def cal_esTime():
    distance = IO.get_distance_from_file(IO.FILENAME)
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