#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:14:09 2020

@author: yingchenliu
"""
import matplotlib.pyplot as plt

from P3 import NaivePriorityQueue
from P3 import HeapPriorityQueue
from P3 import PythonHeapPriorityQueue
from P3 import timeit

nums = (10, 20, 50, 100, 200, 300, 400, 500)

elapsed1 = timeit(ns=nums, pqclass=NaivePriorityQueue)

elapsed2 = timeit(ns=nums, pqclass=HeapPriorityQueue)

elapsed3 = timeit(ns=nums, pqclass=PythonHeapPriorityQueue)


plt.figure(figsize=(8,6))
plt.plot(nums,elapsed1,'.-', label='Naive Priority Queue')
plt.plot(nums,elapsed2,'.-', label='Heap Priority Queue')
plt.plot(nums,elapsed3,'.-', label='Python Heap Priority Queue')
plt.title("Plot Comparing the Three Priority Queue Runtimes")
plt.xlabel("Number of Lists Merged")
plt.ylabel("Elapsed time in seconds")
plt.legend()
plt.savefig('./P3-C.png')
plt.show()
