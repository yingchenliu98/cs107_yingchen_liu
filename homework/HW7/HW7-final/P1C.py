#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 22:33:39 2020

@author: yingchenliu
"""
from Markov import Markov 
import numpy as np
np.random.seed(2000)

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

city_weather_predictions = {}
city_weather_predictions


for k,v in city_weather.items():
   
    weather_data = Markov(v)
    weather_data.load_data()
    counts = dict()
    result = weather_data.get_weather_for_day(7, 100)
    for i in result:
        counts[i] = counts.get(i,0) + 1
    
    city_weather_predictions[k] = counts
print('----------------------------------')
print("The number of occurrences of each weather condition over the 100 trials for each city")
print('----------------------------------')
for k,v in city_weather_predictions.items():
    print(k,':',v)
print('----------------------------------')
print('Most likely weather in seven days\n----------------------------------')
for k,v in city_weather_predictions.items():
    most_likely = max(v,key=v.get)
    print(k,':', most_likely)
    
# initial weather condition
city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}
np.random.seed(2000)
# print occurrences
occurrence_storage = {}
for i, city in enumerate(list(city_weather.keys())):
    occurrence = dict(zip(['sunny', 'cloudy', 'rainy', 'snowy', 'windy', 'hailing'], [0,0,0,0,0,0])) 
    M = Markov(city_weather[city])
    M.load_data()
    wea_sim = M.get_weather_for_day(7, 100)
    for wea in wea_sim:
        occurrence[wea] += 1
    print("%s:" %(city), occurrence)
    occurrence_storage[city] = occurrence

# print most commonly predicted weather
print("\nMost likely weather in seven days\n----------------------------------")
for i, city in enumerate(list(city_weather.keys())):
    max_idx = list(occurrence_storage[city].values()).index(max(list(occurrence_storage[city].values())))
    print("%s:" %(city), list(occurrence_storage[city].keys())[max_idx])