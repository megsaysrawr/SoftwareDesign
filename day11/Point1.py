"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""
import math

class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self,x,y):
        self.x = x
        self.y = y

def print_point(p):
    """Print a Point object in human-readable format."""
    print '(%g, %g)' % (p.x, p.y)

def distance_between_points(p1,p2):
    """Takes two Points as arguments and returns the distance between them."""
    distance = math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
    return distance
    
class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """
    def __init__(self,width,height,corner):
        self.width = width
        self.height = height
        self.corner = corner


def find_center(rect):
    """Returns a Point at the center of a Rectangle."""
    p = Point(0,0)
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight


def main():
    blank = Point(3,4)
    print 'blank',
    print_point(blank)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print 'center',
    print_point(center)

    print box.width
    print box.height
    print 'grow'
    grow_rectangle(box, 50, 100)
    print box.width
    print box.height


if __name__ == '__main__':
    point1 = Point(2,6)    
    point2 = Point(3,5)
  
    distance =  distance_between_points(point1,point2)
    box = Rectangle(10,5,point1)
        
    center_point = find_center(box)
    print '(%g,%g)' % (center_point.x, center_point.y)
    # print 'The distance between is %f' % distance
    # %f means turn it into a float and allows you to put the variable names at the end