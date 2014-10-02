# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 14:02:21 2014

@author: Meg McCauley

Day 8: Turtle World
my_regular_polygon
Write a function called my_regular_polygon that takes as input
the lower lefthand vertex, the side length, and the number of
sides of a regular polygon and draws the polygon to the Turtle world canvas.
"""
from swampy.TurtleWorld import*

def my_regular_polygon(left_x,left_y,side_length,num_sides):
    world = TurtleWorld()
    meg = Turtle()
    meg.delay = 0.1
    meg.x = left_x
    meg.y = left_y
    meg.pen_color = "green"
    for i in range (0,num_sides):  
        meg.fd(side_length)
        meg.rt(360/num_sides)

my_regular_polygon(5,5,40,8)

#Allows Turtle World to stay open after the script ends
running = 1

while running:
    pass