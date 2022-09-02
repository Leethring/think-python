#! python3

"""ex5-6.py - Draw koch curve."""

import turtle

def koch(t, l):
    """Draw a koch curve.
    
    t: turtle object
    l: length of a koch curve.
    """
    if l < 9:
        t.fd(l)
    else:
        koch(t, l/3)
        t.lt(60)
        koch(t, l/3)
        t.rt(120)
        koch(t, l/3)
        t.lt(60)
        koch(t, l/3)

def snowflake(t, l):
    """Draws a snowflake (a triangle with Koch curve for each side."""
    for i in range(3):
        koch(t, l)
        t.rt(120)


bob = turtle.Turtle()
line = input("The total length of Koch curve:")
snowflake(bob, int(line))

turtle.mainloop()