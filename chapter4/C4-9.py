# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:01:09 2019

@author: siddhartha
"""

''''
Problem statement:
    
Write a short recursive Python function that finds the minimum and maximum
values in a sequence without using any loops.
'''

#find minimum in list recursively

def findMinNumber(l):
    
    if len(l) == 0:
        
        raise ValueError('Cannot find min value in empty list')
        
    elif len(l)==1:
        return l[0]
    else:
        minNumber = findMinNumber(l[1:])
        minimum = l[0]
        
        if minNumber < minimum:
            minimum = minNumber
            
        return minimum
    
#find maximum in list recursively     
def findMaxNumber(l):
    
    if len(l)==0:
        raise ValueError('Cannot find max value in empty List')
        
    elif len(l)==1:
        return l[0]
    
    else:
        maxNumber = findMaxNumber(l[1:])
        maximum = l[0]
        if maxNumber > maximum:            
            maximum = maxNumber
        return maximum
    
#test the functions by passing test data
        
listA = [9,-2,6,1,80,9,-2]   

print(findMinNumber(listA))

print(findMaxNumber(listA))