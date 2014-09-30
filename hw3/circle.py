# -*- coding: utf-8 -*-
"""
Homework 3: Data Mining
circle
Created on Mon Sep 29 20:47:47 2014

@author: Meg McCauley
"""
from pattern.web import*
circle = URL('https://www.cs.drexel.edu/~introcs/F2K/placement/circle.txt').download()

import pickle
f = open('circle.pickle','w')
pickle.dump(circle,f)
f.close()
input_file = open('circle.pickle','r')
reload = pickle.load(input_file)

print circle