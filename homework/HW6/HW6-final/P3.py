#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:55:09 2020

@author: yingchenliu
"""

from random import sample
from time import time
import heapq
from P2 import MinHeap
from P2 import MaxHeap
class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        # put should take in a value val and insert it at the end of the elements list.
        if len(self.elements) == self.max_size:
            raise IndexError("Queue is full.")
        else:
            self.elements.append(val)
            
    def get(self):
        if len(self.elements) == 0:
            raise IndexError("Queue is empty.")
        else:
            self.elements.sort()
            return self.elements.pop(0)
        
    def peek(self):
        if len(self.elements) == 0:
            raise IndexError("Queue is empty.")
        else:
            sorted_queue = sorted(self.elements)
            return sorted_queue[0]
        
def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists): 
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i)) 

    return merged


def generatelists(n, length=20, dictionary_path='../data/words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed

class NaivePriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)
        

        
        
class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)
        self.queue = MinHeap(self.elements)
        
    def put(self, val):
        if len(self.queue) == self.max_size:
            raise IndexError("Queue is full.")
        else:     
            self.queue.heappush(val)
            
    def get(self):
        if len(self.queue) == 0:
            raise IndexError("Queue is empty.")
        else:
            return self.queue.heappop()
            
    def peek(self):
        if len(self.queue) == 0:
            raise IndexError("Queue is empty.")
        else:
            return self.queue.elements[0]
        
class PythonHeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)
        
    def put(self, val):
        if len(self.elements) == self.max_size:
            raise IndexError("Queue is full.")
        else:     
            heapq.heappush(self.elements,val)
            
    def get(self):
        if len(self.elements) == 0:
            raise IndexError("Queue is empty.")
        else:
            return heapq.heappop(self.elements)
            
    def peek(self):
        if len(self.elements) == 0:
            raise IndexError("Queue is empty.")
        else:
            #return heapq.nsmallest(1, self.elements)[0]
            return self.elements[0]
        
        
        
# demo       
# if __name__ == "__main__":
#     print("<<<<<<<<<<<<<<part A>>>>>>>>>>>>>>")
#     q = NaivePriorityQueue(4)
#     q.put(1)
#     q.put(2)
#     q.put(5)
#     q.put(-1)
#     print(q.peek())
#     print(q.elements)
#     print(q.get())
#     print(q.get())
#     print(q.get()) 
#     print(q.elements)
#     print("<<<<<<<<<<<<<<part B>>>>>>>>>>>>>>")
#     q = HeapPriorityQueue(5)
#     q.put(1)
#     q.put(-10)
#     q.put(1)
#     q.put(20)
  
#     print(q.peek())
#     print(q.elements)
#     print(q.get())
#     print(q.get())
#     print(q.get()) 

#     print(q.get()) 
#     print(q.elements)
#     print("<<<<<<<<<<<<<<part C>>>>>>>>>>>>>>")
#     q = PythonHeapPriorityQueue(6)
#     q.put(1)
#     q.put(-10)
#     q.put(1)
#     q.put(20)
#     q.put(20)
#     print(q.peek())
#     print(q.elements)
#     print(q.get())
#     print(q.get())
#     print(q.get()) 
#     print(q.get()) 
#     print(q.get()) 
#     print(q.elements)

  