#! python3
# ex4-3.py - Draws a polymer with separated triangles.

import turtle
import math

# todo: Def a class that draws a triangle.
class triangle():
    def __init__(self, t, b, v):
        """Def a triangle class
        
        b: base of a triangle
        v: vertex angle of a triangle
        t: turtle object
        """
        self.base = b
        self.vertex = v
        self.turtle = t
        self.baseAngle = (180 - v) / 2
        self.leg = (self.base / 2) / math.cos(self.baseAngle * (math.pi/180))
    
    def draw(self):
        """Draws a triangle."""
        self.turtle.fd(self.leg)
        self.turtle.lt(180 - self.baseAngle)
        self.turtle.fd(self.base)
        self.turtle.lt(180 - self.baseAngle)
        self.turtle.fd(self.leg)
        self.turtle.lt(180)

# todo: Def a function that draws a polymer.
def drawPolymer(t, n):
    """Draws a polymer.
    
    t: Triangle object
    n: The number of triangles
    """
    t.turtle.lt(t.vertex / 2)
    for i in range(n):
        t.draw()

# Draw a polymer

if __name__ == "__main__":
    
    bob = turtle.Turtle()
    print('The base of a triangle:')
    baseLine_str = input()
    baseLine = int(baseLine_str)
    print('How many triangles:')
    n_str = input()
    n = int(n_str)
    angleT = 360 / n

    tri1 = triangle(bob, baseLine, angleT)
    drawPolymer(tri1, n)

    turtle.mainloop()
    