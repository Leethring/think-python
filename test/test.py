import turtle
from polygon import arc

class petal():
    """Draws a petal.
    
    t: turtle object
    r: arc radius. Determinate the length of a petal
    a: arc angle. Determinate the width of a petal
    """
    def __init__(self, t, r, a):
        self.turtle = t
        self.radius = r
        self.angle = a

#    def draw():
#        turnBack = 180 - self.angle
#        for i in range(2):
#            arc(t, r, a)
#            t.lt(turnBack)

bob = turtle.Turtle()

radius = 5
angle = 30

petal1 = petal(bob, 5, 30)

print(petal1.radius)