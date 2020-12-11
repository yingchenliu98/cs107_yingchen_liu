 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:25:27 2020

@author: yingchenliu
"""
# Import the Markov class from Markov.py
from Markov import Markov 
import numpy as np

# Load the provided weather.csv file into a numpy array
weather = np.genfromtxt('./weather.csv',delimiter=',',names=['sunny', 'cloudy', 'rainy', 'snowy', 'windy', 'hailing'])
#display(weather)

#Demonstrate that your Markov class works by printing the probability that a windy day follows a cloudy day.
weather_data = Markov()
weather_data.load_data()
print("The probability that a windy day follows a cloudy day is: ", weather_data.get_prob('windy', 'cloudy')) 
# print("The probability that a windy day follows a cloudy day is: ", weather_data.get_prob('WINDY', 'cloudy')) # upper case
# print("The probability that a windy day follows a cloudy day is: ", weather_data.get_prob('sd', 'cloudy')) # raise exception
