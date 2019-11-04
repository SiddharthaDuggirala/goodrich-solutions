# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 23:56:31 2019

@author: pcs
"""


def reverse(word):
    
    if len(word)==0:
        return word
    return reverse(word[1:])+word[0]


def palindrome(word):
    
    return (word ==reverse(word)) 

print(palindrome('gohangasalamiimalasagnahog'))