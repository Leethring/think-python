#! python3
# ex4-exp1.py - Draws a square

# Requirement:
# Create a function called 'square'
# Square takes a parameter named 't'
# Create a function called 'bob' as an argument to square
# bob is a turtle object

import turtle

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
    turtle.mainloop()

bob = turtle.Turtle()

square(bob)