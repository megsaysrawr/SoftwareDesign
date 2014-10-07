# -*- coding: utf-8 -*-
"""
Random_art.py

@author: Meg McCauley
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
import math

def build_random_function(min_depth, max_depth):
    """ Inputs: min_depth, max_depth (used to determine the regression depth)
        Output: Returns a function as determined by a random generator.
    """

    temp_var = [['x'],['y']]
    if max_depth <= 1:
        return temp_var[randint(0,1)]
    a = build_random_function(min_depth-1,max_depth-1)
    b = build_random_function(min_depth-1,max_depth-1)
    prod = ['prod',a,b]
    cos_pi = ['cos_pi',a]
    sin_pi = ['sin_pi',a]
    cubed = ['cubed',a]
    sqrt = ['sqrt',a]
    function_list = [prod,cos_pi,sin_pi,cubed,sqrt,['x'],['y']]
    if min_depth > 1:
        return function_list[randint(0,4)]
    else: 
        return function_list[randint(0,6)]

def evaluate_random_function(f, x, y):
    """ Inputs: f = random function
                x = value of x
                y = value of y
        Output: the value of f evaluated for x,y
    """

    first_term = f[0]
    if first_term == 'x':
        return x
    if first_term == 'y':
        return y
    if first_term == 'prod':
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    if first_term == 'cos_pi':
        return math.cos(math.pi*evaluate_random_function(f[1],x,y))
    if first_term == 'sin_pi':
        return math.sin(math.pi*evaluate_random_function(f[1],x,y))
    if first_term == 'cubed':
        return evaluate_random_function(f[1],x,y)**3.0
    if first_term == 'sqrt':
        return math.sqrt(evaluate_random_function(f[1],x,y))


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
    # Making sure that all variables can print with decimals by making them floats
    val = float(val)
    input_interval_start = float(input_interval_start)
    input_interval_end = float(input_interval_end)
    output_interval_start = float(output_interval_start)
    output_interval_end = float(output_interval_end)

    x = val - input_interval_start
    y = input_interval_end - input_interval_start
    z = output_interval_end - output_interval_start
    c = output_interval_start

    f = (x/y) * z + c
    return f

def create_art(xsize,ysize,min_depth,max_depth):
    xsize = int(xsize)
    ysize = int(ysize)

    red = build_random_function(min_depth,max_depth)
    blue = build_random_function(min_depth,max_depth)
    green = build_random_function(min_depth,max_depth)
    print red, blue, green
    image = Image.new("RGB",(xsize,ysize))
    for i in range(xsize):
        x = remap_interval(i,00,xsize,0,1.0)
        for j in range(ysize):
            y = remap_interval(i,0.0,ysize,0,1.0)

            eval_red = evaluate_random_function(red,x,y)
            eval_blue = evaluate_random_function(blue,x,y)
            eval_green = evaluate_random_function(green,x,y)

            redmap = remap_interval(eval_red,0,1,0,255)
            bluemap = remap_interval(eval_blue,0,1,0,255)
            greenmap = remap_interval(eval_green,0,1,0,255)

            image.putpixel((i,j),(int(redmap),int(bluemap),int(greenmap)))
        image.save('image'+str(2)+'.jpg')

create_art(1000,1000,1,10)