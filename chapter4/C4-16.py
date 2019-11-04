# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 23:30:44 2019

@author: siddhartha
"""

def reverse(word):
    
    if len(word)==0:
        return word
    else:
        return reverse(word[1:])+word[0]
    
print(reverse('snap&stop'))