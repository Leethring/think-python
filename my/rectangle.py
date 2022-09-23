import turtle

def rectangle(t, length, width):
    """Draw a rectangle.

    Information
    ---
    This function draws a rectangle by using turtle module. 

    Input
    ---
    t: Turtle
        A turtle object used for drawing
            
    length: float
        The length of a rectangle
    
    width: float
        The width of a rectangle

    Output | Showing | Presentation
    ---
    output: image
        A rectangle drawn by a turtle
    """
    for i in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(width)
        t.lt(90)

if __name__ == '__main__':
    # Draw a rectangle with length 100 and width 50
    a = turtle.Turtle()
    rectangle(a, 100, 50)
    turtle.mainloop()