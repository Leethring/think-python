#! python

# ex4-2.py - Draws a flower with polygon

import turtle 

from polygon import arc

def petal(t, r, a):
    """Draws a petal.
    
    t: turtle object
    r: arc radius. Determinate the length of a petal
    a: arc angle. Determinate the width of a petal
    """
    arc(t, r, a)
    turnBack = 180 - a
    t.lt(turnBack)
    arc(t, r, a)

def flower(t, r, a, p):
    """Draws a flower.
    
    t: turtle object
    r: radius. 
    a: arc angle. Determinate the number of petals
    p: the number of petals
    """
    petal_angle = 360 / p
    for i in range(p):
        petal(t, r, a)
        turnBack = 180 - a
        t.lt(turnBack)
        t.lt(petal_angle)


if __name__ == '__main__':

    bob = turtle.Turtle()

    print('You will create a flower.')
    print('You need to input a arc length and a arc angle to form a petal.')
    print('You need to input petal angle to form a flower.')
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

    flower(bob, arc_radius, arc_angle, petals)
    turtle.mainloop()