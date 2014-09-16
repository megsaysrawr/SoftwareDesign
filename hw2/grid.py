"""
grid.py
Think Python, Exercise 3.5
author = Meg McCauley
"""

def plusMinusRow(cols):
    segment = '+ ' + '- '*4
    fullRow = segment * cols + '+'
    print fullRow
    
def printPipeRows(cols):
    for i in range(4):  
        segment2 = '|' + ' '*9
        fullRow2 = segment2 * cols + '|'
        print fullRow2
    
def grid(rows,cols): #Creates a grid 
    for i in range(rows):
        plusMinusRow(cols)
        printPipeRows(cols)
    plusMinusRow(cols)
     
userRows = input("How many rows? ")
userCols = input("How many columns? ")
grid(userRows,userCols)