#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 01:51:41 2020

@author: yingchenliu
"""
from P4 import init_length 
import matplotlib.pyplot as plt
import datetime

a_minute = 60
while a_minute > 0:
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
    
    a_minute -= 1
    
    # Plot the clock
    
    fig = plt.figure(figsize=(6,6))
    fig.canvas.draw()
    plt.cla()
    plt.axis('off')
    plt.axis([-5, 5, -5, 5])
    plt.plot([0, x_hour],[0,y_hour],lw='6')
    plt.plot([0, x_min], [0,y_min],lw='4')
    plt.plot([0, x_sec],[0,y_sec],lw='1')
   
    plt.pause(0.1)
    
    
    print(a_minute)