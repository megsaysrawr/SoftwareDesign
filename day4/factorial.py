# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:32:31 2014

@author: Meg McCauley

Returns n!
"""
def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac*i
    return fac

print factorial(4)
