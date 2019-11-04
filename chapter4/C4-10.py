# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:35:12 2019

@author: siddhartha
"""

#----------------------------------------
#Describe a recursive algorithm to compute the integer part of the base-two
#logarithm of n using only addition and integer division.
#----------------------------------------

def calcLog(x,a):
    
    if x<a:
        return 0
    return 1+calcLog(x/a,a)

print(calcLog(100,2))

