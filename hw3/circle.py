# -*- coding: utf-8 -*-
"""
Homework 3: Data Mining
circle
Created on Mon Sep 29 20:47:47 2014

@author: Meg McCauley
"""
import array
from pattern.web import*
"""
circle = URL('https://www.cs.drexel.edu/~introcs/F2K/placement/circle.txt').download()

import pickle
f = open('circle.pickle','w')
pickle.dump(circle,f)
f.close()
input_file = open('circle.pickle','r')
reload = pickle.load(input_file)
"""

def get_offline_snippet():
    circle = open('/home/megsaysrawr/SoftwareDesign/hw3/circle.pickle','r')
    return circle
    
snippet = get_offline_snippet()
#print snippet

s = 'Once, upon. T \"sasdf' 

line = s.translate(None, '!@#$,."')
print line

#Test of GitHub
