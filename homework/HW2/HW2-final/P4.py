#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:07:57 2020

@author: yingchenliu
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime


### Closure defined up here
def init_length(length_of_hand):
    def compute_radians(theta):
        """
        Parameters: theta(float): the angle of the clock hand 
        Returns: (x,y) coordinate of the clock hand on the circle
        """
        r = length_of_hand
        
        theta_h = np.pi * theta/180
        
        x = r * np.cos(theta_h)
        y = r * np.sin(theta_h)
        
        return (x, y)
    return compute_radians



currentDT = datetime.datetime.now()
hour = currentDT.hour
minute = currentDT.minute
second = currentDT.second

# Calculate theta in degrees for each hand
theta_hour = 90 - 30 * hour - minute/2
theta_min = 90 - 6 * minute
theta_sec = 90 - 6 * second

# Specify the length of hour, minute and second hands
hand_h, hand_m, hand_s = (3, 4, 5)

hour_hand = init_length(hand_h)
min_hand = init_length(hand_m)
sec_hand = init_length(hand_s)
x_hour, y_hour = hour_hand(theta_hour)
x_min, y_min = min_hand(theta_min)
x_sec, y_sec = sec_hand(theta_sec)

# Plot the clock

fig = plt.figure(figsize=(6,6))
plt.axis('off')
plt.axis([-5, 5, -5, 5])
plt.plot([0, x_hour],[0,y_hour],lw='6')
plt.plot([0, x_min], [0,y_min],lw='4')
plt.plot([0, x_sec],[0,y_sec],lw='1')
plt.show()