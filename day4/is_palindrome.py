# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:54:50 2014

@author: Meg McCauley
"""
def is_palindrome(x):
    """
    Returns true iff the string x is a palindrome
    """
    return (x==x[::-1]) #[::-1] reverses the word
    
print is_palindrome('hannah')
print is_palindrome('dinosaur')
