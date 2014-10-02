# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 14:02:21 2014

@author: Meg McCauley

Day 8: Turtle World
my_square
Write a function called my_square that takes as input the coordinates
of the lower lefthand corner and the side length of a square and draws
the square to the Turtle world canvas.
"""
from swampy.TurtleWorld import*

def my_square(left_x,left_y,side_length):
    world = TurtleWorld()
    meg = Turtle()
    meg.delay = 0.1
    meg.x = left_x
    meg.y = left_y
    meg.pen_color = "green"
    for i in range (0,4):  
        meg.fd(side_length)
        meg.rt(90)

my_square(1,5,40)

#Allows Turtle World to stay open after the script ends
running = 1

while running:
    pass