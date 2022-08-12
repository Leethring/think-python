#! python3
# ex4-exp2.py - Draws a square

import turtle

def square(t, length):
    """Draws a square.

    t: turtle object
    length: Length of a square
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

bob = turtle.Turtle()

length = 120
square(bob, length)