"""
fermat.py
Think Python, Exercise 5.3
author = megsaysrawr
"""

def check_fermat(a,b,c,n):
    aPower = a**n
    bPower = b**n
    cPower = c**n    
    if n>2 and aPower+bPower==cPower:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."
        
# check_fermat(1,2,3,4) #Test case

# Take user input for test cases
userA = input('Input the a value: ')
userB = input('Input the b value: ')
userC = input('Input the c value: ')
userN = input('Input the n value: ')

check_fermat(userA,userB,userC,userN)