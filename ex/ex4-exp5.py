#! python3
# ex4-exp5.py - Draws a arc

import turtle
import math

def arc(t, r, angle):
    """Draws a arc with specific angle.
    
    angle: The angle of a arc. 
    
    If the angle = 360, the arc function draw a circle.
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, length, n):
    """Draws a polygon.

    t: turtle object
    length: Length of a square
    n: the sides of a polygon
    """
    ang = 360 / n
    polyline(t, n, length, ang)
    
def circle(t, r):
    """Draws circle, which is a arc with 360 degree
    
    t: turtle object
    r: radius of a circle
    """
    arc(t, r, 360)

bob = turtle.Turtle()

r = 50
angle = 180
arc(bob, r, angle)
polygon(bob, 50, 4)
circle(bob, 60)

turtle.mainloop()