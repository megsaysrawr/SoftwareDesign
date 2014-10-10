# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 14:48:19 2014

@author: Meg McCauley
"""
from pattern.web import*
from pattern.en import parse

def get_book():
    anne_of_green_gables = URL('http://www.gutenberg.org/cache/epub/45/pg45.txt').download()
    
    # Save snippet by pickling it
    f = open('riddle.pickle','r')
    full_text_anne = f.read()
    f.close()
    return full_text_anne
    
get_book()