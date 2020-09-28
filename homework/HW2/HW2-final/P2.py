#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 23:30:24 2020

@author: yingchenliu
"""

def dna_complement(sequence):
    """
    Parameters
    ----------
    sequence(str): a string of arbirary length representing a DNA sequence
   
    Returns:
    ----------
    ret(str): a string of the corresponding DNA complement

    """
    
    if sequence:
        dna = sequence.upper()
    else:
       return None
   
    dna_bases = 'ATGC'
    
    for char in dna:
        if char not in dna_bases:
            return None

    complements = {"A":"T", 
                   "T":"A", 
                   "G":"C", 
                   "C":"G"}
    ret = ''
    for char in dna:
        ret += complements[char]
    
    return ret

## demo1
test1 = 'acTG'
print('The input DNA sequence is: ', test1)
print('The output complement DNA sequence is :', dna_complement(test1))
## demo2
test2 = 'asdmketgc'
print('The input DNA sequence is: ', test2)
print('The output complement DNA sequence is :', dna_complement(test2))