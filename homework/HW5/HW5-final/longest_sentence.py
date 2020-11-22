#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:30:12 2020

@author: yingchenliu
"""
from linked_list import LinkedList
from linked_list import Nil
def get_list_of_sentences(chapter1='swansway-chapter1.txt'):
    def to_sentences(p):
            for delimiter in '.?!': p = p.replace(delimiter, '|')
            return [s.strip('\" ') for s in p.split('|')]
    with open(chapter1, 'r', encoding='UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)

    return list_of_sentences


def longest_sentence():
    
    def num_words(x):
        words = x.split()
        return len(words)
    
    def bigger(a,b):
        return a if a > b else b
    
    list_of_sentences = get_list_of_sentences()  
    length = list_of_sentences.for_each(num_words)
    return length.reduce_right(bigger)


if __name__ == '__main__':
    print(f"The longest sentence has {longest_sentence()} words.")