#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:25:28 2020

@author: yingchenliu
"""
import numpy as np
class Markov:

    def __init__(self, day_zero_weather=None): # You will need to modify this header line later in Part C
        self.data = None
        self.day_zero_weather = day_zero_weather
        self.weather = ['sunny', 'cloudy', 'rainy', 'snowy', 'windy', 'hailing']
        # Your implementation here

    def load_data(self, file_path='./weather.csv'):
        self.data =  np.genfromtxt(file_path,delimiter=',')

    def get_prob(self, current_day_weather, next_day_weather): 
        if current_day_weather != None and next_day_weather !=None:
            current_day_weather = current_day_weather.lower()
            next_day_weather = next_day_weather.lower()
            
            if current_day_weather not in self.weather:
                raise ValueError("The current day weather is not in the weather list.")
                
            if next_day_weather not in self.weather:
                raise ValueError("The next day weather is not in the weather list.")
                
            row_idx = self.weather.index(current_day_weather)
            col_idx = self.weather.index(next_day_weather)
            
            return self.data[row_idx][col_idx]
        else:
            raise ValueError('Enter the weathers to get the probability!')
        

    def __iter__(self):
        ''' Returns the Iterator object '''
        return MarkovIterator(self)
    
    def _simulate_weather_for_day(self, day):
        if isinstance(day, int):
            if day < 0:
                raise ValueError("Please enter a positive day.")
            
            if day == 0:
                return self.day_zero_weather
            
            else:
                iterator = iter(self)
                while day>=1:
                    elem = next(iterator)
                    day -= 1
                return elem
        else:
            raise ValueError('Day should be an integer.')
                
    def get_weather_for_day(self, day, trials=1):
        predictions = []
        while trials > 0:
            predictions.append(self._simulate_weather_for_day(day))
            trials-=1
        return predictions
        

class MarkovIterator:
    def __init__(self, markov):
        self.markov = markov
        self.curr_day = markov.day_zero_weather
        
    def __iter__(self):            
        return self
        
    def __next__(self):
        if self.curr_day is None:
            raise ValueError("Please enter the current day.")
      
        self.curr_day = np.random.choice(self.markov.weather, 
                                          p=self.markov.data[self.markov.weather.index(self.curr_day)]) 
            
        return self.curr_day

