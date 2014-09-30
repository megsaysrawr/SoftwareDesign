# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:44:22 2014

@author: Meg McCauley

Returns True iff n is a prime number
"""
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
print is_prime(7)