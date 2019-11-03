# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:48:22 2019

@author: pcs
"""

def multiplication(n,m):
    
    if (m==0):
        return 0
    elif m<0:
        return -(n - multiplication(n,m+1))
    else:
        return n +multiplication(n,m-1)
    

print(multiplication(4,-6))
        
        