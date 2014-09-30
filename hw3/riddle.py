# -*- coding: utf-8 -*-
"""
Homework 3: Data Mining
riddle
Created on Mon Sep 29 20:47:47 2014

@author: Meg McCauley
"""
from pattern.web import*
riddle = URL('https://www.cs.drexel.edu/~introcs/F2K/placement/riddle.txt').download()

import pickle
f = open('riddle.pickle','w')
pickle.dump(riddle,f)
f.close()
input_file = open('riddle.pickle','r')
reload = pickle.load(input_file)

print riddle