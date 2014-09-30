# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:32:31 2014

@author: Meg McCauley

Returns the sum of all integers in the range [x,y]
"""
def sum_integers(x,y):
    sum = 0
    for i in range(x,y+1):
        sum = sum + i
    return sum
print sum_integers(2,5)