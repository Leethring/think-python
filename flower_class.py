#! python

# ex4-2.py - Draws a flower with polygon

import turtle 

from polygon import arc

class petal():
    def __init__(self, t, r, a):
        """A petal
        
        t: turtle object
        r: arc radius. Determinate the length of a petal
        a: arc angle. Determinate the width of a petal
        """
        self.turtle = t
        self.radius = r
        self.angle = a

    def draw(self):
        """Draws a petal."""
        turnBack = 180 - self.angle
        for i in range(2):
            arc(self.turtle, self.radius, self.angle)
            self.turtle.lt(turnBack)

def flower(p, n):
    """Draws a flower.
    
    p: petal object
    n: number of petals
    """
    petal_angle = 360 / n
    for i in range(n):
        p.draw()
        p.turtle.lt(petal_angle)


if __name__ == '__main__':

    bob = turtle.Turtle()

    print('You will create a flower.')
    print('You need to input a arc length and a arc angle to form a petal.')
    print('You need to input the number of a flower.')
    # todo: Get the arc length, arc angle, petal angle from input 
    print("Please input the arc radius: ")
    arc_radius_str = input()
    arc_radius = int(arc_radius_str)
    print('Please input the arc angle:')
    arc_angle_str = input()
    arc_angle = int(arc_angle_str)
    print('Please input the number of petals:')
    petals_str = input()
    petals = int(petals_str)

    petal1 = petal(bob, arc_radius, arc_angle)
    flower(petal1, petals)
    turtle.mainloop()