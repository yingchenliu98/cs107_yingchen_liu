#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:42:20 2020

@author: yingchenliu
"""

from math import floor
from typing import List

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size
    def compare(self, a: int, b: int) -> bool:
        pass
    # TODO: override this in your dervied classes
    def heapify(self, idx: int) -> None:
        # TODO: implement
        # maintains the max/min-heap property
        largest = idx
        l = self.left(idx)
        r = self.right(idx)
        if l < self.size and self.compare(self.elements[largest], self.elements[l]):
            largest = l
        if r < self.size and self.compare(self.elements[largest], self.elements[r]):
            largest = r
        if largest != idx:
            self.swap(idx, largest)
            self.heapify(largest)
        
    def build_heap(self) -> None:
        # TODO: implement

        for i in range(floor(self.size/2), -1, -1):
            # print(i)
            self.heapify(i)
            

    def heappush(self, key: int) -> None:
        # TODO: implement
        # inserts a new element into the heap (while maintining its heap-property!)
   
        self.elements.append(key)
        self.size += 1
        temp_node = len(self.elements) - 1
        while self.parent(temp_node) >= 0 and self.compare(self.elements[self.parent(temp_node)],self.elements[temp_node]):
            self.swap(temp_node, self.parent(temp_node))
            temp_node = self.parent(temp_node)       
    
            
    def heappop(self) -> int:
        # TODO: implement
        # this function should remove the heap's minimum element and return it to the caller
        # Raise an IndexError when trying to pop from an empty heap
        if len(self.elements) == 0:
            raise IndexError("Empty heap.")
        else:
            
            lastelt = self.elements.pop()
            if self.elements:
                returnitem = self.elements[0]
                self.size -= 1
                self.elements[0]=lastelt
                self.heapify(0)
                return returnitem
            return lastelt
        

class MinHeap(Heap):
    # TODO: complete implementation
    def __init__(self, array: List[int]):
        super().__init__(array)
    def compare(self, a: int, b: int) -> bool:
        return a > b 

class MaxHeap(Heap):
    # TODO: complete implementation
    def __init__(self, array: List[int]):
        super().__init__(array)
    def compare(self, a: int, b: int) -> bool:
        return a < b 
# demo
   
# if __name__ == "__main__":
#     print("<<<<<<<<<<<<<<part A>>>>>>>>>>>>>>")
#     h1 = MinHeap([-1,0,0,15,23,1,2,3]) # The heap tree will be built during initialization
#     print(h1)
    
#     h2 = MinHeap([9,-3,7,-2,0,5,3,1,-9,3]) # The heap tree will be built during initialization
#     print(h2)
    
#     print("<<<<<<<<<<<<<<part B>>>>>>>>>>>>>>")
#     h1.heappush(10)
#     print("push 10: \n",h1)
    
#     h1.heappush(-6)
#     print("push -6: \n", h1)
    
#     h1.heappush(-10)
#     print("push -10: \n", h1)
    
#     h1.heappop()
#     print("pop once:\n", h1)
#     h1.heappop()
    
#     print("pop twice:\n", h1)
    
#     print("<<<<<<<<<<<<<<part C>>>>>>>>>>>>>>")
#     h3 = MaxHeap([-1,0,0,15,23,1,2,3])
    
#     mn = MinHeap([1,2,3,4,5])
#     mx = MaxHeap([1,2,3,4,5])

#     print("minheap:\n",mn)
#     print("maxheap:\n",mx)

