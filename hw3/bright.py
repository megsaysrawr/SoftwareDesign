# -*- coding: utf-8 -*-
"""
Homework 3: Data Mining
bright
Created on Mon Sep 29 20:47:47 2014

@author: Meg McCauley
"""
from pattern.web import*
bright = URL('https://www.cs.drexel.edu/~introcs/F2K/placement/bright.txt').download()

import pickle
f = open('bright.pickle','w')
pickle.dump(bright,f)
f.close()
input_file = open('bright.pickle','r')
reload = pickle.load(input_file)

print bright