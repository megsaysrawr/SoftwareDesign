# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 14:02:21 2014

@author: Meg McCauley

Day 8: Turtle World
my_circle
Write a function called my_circle that takes as input the center and
radius of a circle and draws the circle to the canvas by approximating
a circle as a regular polygon of a large number of sides.
"""
from swampy.TurtleWorld import*
import math

def my_circle(center_x,center_y,radius):
    world = TurtleWorld()
    meg = Turtle()
    meg.delay = 0.1
    meg.x = center_x
    meg.y = center_y
    meg.pen_color = "blue"
    num_sides = 50
    side_length = (2*math.pi*radius)/num_sides
    for i in range (0,num_sides):  
        meg.fd(radius)
        meg.rt(360/num_sides)

my_circle(0,0,10)

#Allows Turtle World to stay open after the script ends
running = 1

while running:
    pass