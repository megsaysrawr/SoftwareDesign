# -*- coding: utf-8 -*-
"""
This codeshare is being used by SoftDes Fall 2014 to work on a brickbreaker example

Created on Tue Oct 14 2014

@author: Amon Millner, building upon Paul Ruvolo’s Spring 2014 SoftDes example
"""

import pygame
from pygame.locals import *
import random
import math
import time

class BrickBreakerModel:
    """ Encodes the game state """
    def __init__(self, brick_color):
        self.bricks = []
        for x in range(10,800,100):
            brick = Brick(brick_color,20,80,x,100)
            self.bricks.append(brick)
            brick = Brick(brick_color,20,80,x,75)
            self.bricks.append(brick)
            brick = Brick(brick_color,20,80,x,50)
            self.bricks.append(brick)
            brick = Brick(brick_color,20,80,x,25)
            self.bricks.append(brick)
            
        self.paddle = Paddle((255,255,255),20,100,200,450)

class Brick:
    """ Encodes the state of a brick in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class Paddle:
    """ Encodes the state of the paddle in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        
class Ball:
    """Encodes the state of the ball in the game"""
    def __init__(self,radius):
        self.radius = radius
            
class PyGameWindowView:
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        for brick in self.model.bricks:
            pygame.draw.rect(self.screen, pygame.Color(brick.color[0],brick.color[1],brick.color[2]),pygame.Rect(brick.x,brick.y,brick.width,brick.height))
        pygame.draw.rect(self.screen, pygame.Color(self.model.paddle.color[0],self.model.paddle.color[1],self.model.paddle.color[2]),pygame.Rect(self.model.paddle.x,self.model.paddle.y,self.model.paddle.width,self.model.paddle.height))     
        pygame.display.update()

class PyGameMouseController:
    def __init__(self,model):
        self.model = model
    
    def handle_mouse_event(self,event):
        if event.type == MOUSEMOTION:
            self.model.paddle.x = event.pos[0] - self.model.paddle.width/2.0

if __name__ == '__main__':
    pygame.init()

    size = (700,480)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Brick Breaker')


    model = BrickBreakerModel((100,100,250))
    view = PyGameWindowView(model,screen)
    controller = PyGameMouseController(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == MOUSEMOTION:
                controller.handle_mouse_event(event)
        view.draw()
        time.sleep(.001)
        
    #pygame.quit()