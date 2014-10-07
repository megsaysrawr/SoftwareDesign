# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 14:02:21 2014

@author: Meg McCauley

Day 8: Turtle World
snow_flake
Write a function called my_circle that takes as input the center and
radius of a circle and draws the circle to the canvas by approximating
a circle as a regular polygon of a large number of sides.
"""
from swampy.TurtleWorld import*

world = TurtleWorld()
turtle = Turtle()
turtle.delay = 0.1
turtle.pen_color = "blue"

def snow_flake_side(turtle,length,d):
    """ Draw a side of the snowflake curve with side length l and recursion depth of level """
    if d == 1:
        draw_triangle(turtle,d,length)
        return
    else:
        return snow_flake_side(turtle,1/3*length,d-1)
        
def draw_triangle(turtle,d,length):
    if d == 1:
        turtle.fd(length)
    else:
        drawTriangle(turtle,d-1,length/3)
        
snow_flake_side(0,0,10)

#Allows Turtle World to stay open after the script ends
running = 1

while running:
    pass