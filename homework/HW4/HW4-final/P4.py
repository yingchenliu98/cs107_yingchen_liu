#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:06:07 2020

@author: yingchenliu
"""

class AutoDiffToy():
    
    def __init__(self, a, d=1.0):
        self.val = a
        self.der = d
       
    def __add__(self, other):
        
        try:   
            val = self.val + other.val
            der = self.der + other.der

            return AutoDiffToy(val, der)
        except AttributeError:
         
            other = AutoDiffToy(other, 0)
            val = self.val + other.val
            der = self.der + other.der
 
            return AutoDiffToy(val, der)
        
    def __radd__(self, other): #ensure commutativity of addition
        return self.__add__(other)
    
    def __mul__(self, other):
        try:
            val = self.val * other.val
            der = self.val * other.der + other.val * self.der
        
            return AutoDiffToy(val, der)
        
        except AttributeError:
         
            other = AutoDiffToy(other, 0)
            val = self.val * other.val
            der = self.val * other.der + other.val * self.der

            return AutoDiffToy(val, der)
     
    def __rmul__(self, other):
        return self.__mul__(other)
    
    
if __name__ == '__main__':
    
    # demo
    a = 2.0 
    x = AutoDiffToy(a)
    
    alpha = 2.0
    beta = 3.0
    
    f = alpha * x + beta
    print(f.val, f.der)
    
    f = alpha * x + beta
    print(f.val, f.der)
    
    f = x * alpha + beta
    print(f.val, f.der)
    
    f = beta + alpha * x
    print(f.val, f.der)
    
    f = beta + x * alpha
    print(f.val, f.der)