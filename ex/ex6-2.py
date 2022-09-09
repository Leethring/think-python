# ex6-2.py - def a Ackermann function

def ack(m, n):
    """Evaluate a Ackermann function.
    """
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    
print(ack(3,4))