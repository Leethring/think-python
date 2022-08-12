#! python3
# ex4-exp3.py - Draws a polygon

import turtle

def polygon(t, length, n):
    """Draws a polygon.

    t: turtle object
    length: Length of a square
    n: the sides of a polygon
    """
    ang = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(ang)
    turtle.mainloop()


bob = turtle.Turtle()

length = 120
n = 6
polygon(bob, length, 6)