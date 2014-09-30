# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:21:36 2014

@author: Meg McCauley
"""

def is_between(x,y,z):
    if x <= y and y <= z:
        return True
    else:
        return False

print is_between(1,2,3)