#! python3
# ex4-exp4.py - Draws a approximate circle

import turtle
import math

def polygon(t, length, n):
    """Draws a polygon.

    t: turtle object
    length: Length of a square
    n: the sides of a polygon
    """
    ang = 360 / n
    for i in range(int(n)):
        t.fd(length)
        t.lt(ang)

def circle(t, r):
    """Draws a circle using polygon function.
    
    t: turtle object
    r: radius of the circle
    """
    circumference = 2 * math.pi * r
    # Choose a proper number for sides to draw a circle.
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, length, n)

bob = turtle.Turtle()

r = 50 
circle(bob, r)
turtle.mainloop()