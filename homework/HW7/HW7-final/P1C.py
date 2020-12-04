#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 22:33:39 2020

@author: yingchenliu
"""
from Markov import Markov 


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
    
