#! python3

"""ex5-3.py - Checks could three numbers form a triangle."""

def is_triangle(a, b, c):
    """Check triangle.
    
    a: one side of a triangle
    b: one side of a triangle
    c: one side of a triangle
    """
    print("Can these three lines form triangle?")
    if a + b < c:
        print("No")
    elif a + c < b:
        print("No")
    elif b + c < a:
        print("No")
    else:
        print("Yes")

side1 = input('Please input a integer as side 1 of a triangle:')
side2 = input('Please input a integer as side 2 of a triangle:')
side3 = input('Please input a integer as side 3 of a triangle:')
is_triangle(int(side1), int(side2), int(side3))
