"""
grid.py
Think Python, Exercise 3.5
author = megsaysrawr
"""

def topMiddleBottomRow(): #Creates the top, middle, and bottom rows
    segment = '+ ' + '- '*4
    fullRow = segment * 2 + '+'
    print fullRow

def pipeRow(): #Creates the rows with pipes
    segment2 = '|' + ' '*9
    fullRow2 = segment2 * 2 + '|'
    print fullRow2
    
def rowMultipler(repeat): #Outputs a function a user defined number of times
    for i in range(0,repeat):
        pipeRow()
    

topMiddleBottomRow()
rowMultipler(4)
topMiddleBottomRow()
rowMultipler(4)
topMiddleBottomRow()