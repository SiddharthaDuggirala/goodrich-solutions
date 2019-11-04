# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:19:57 2019

@author: siddhartha
"""


def uniqueness(l):
    
    if len(l) == 1:
        return True
    elif l[0] in l[1:]:
        return False
    else:
        return uniqueness(l[1:])
    

lst = [1,2,3,4,5,6,6]

print(uniqueness(lst))
           