"""Return True if a is the power of b.

a is a power of b if a is divisible by b and a/b is the power of b.
"""

def is_power(a, b):
    """Return True if a is the power b.
    
    Parameters
    ---
    a: int
        A number
    b: int
        A number
    """
    if a == b:
        return True
    elif a % b == 0:
        return is_power(a/b, b)
    else:
        return False

if __name__ == "__main__":
    print(f'128 is the power of 2: {is_power(128, 2)}')
    print(f'63 is the power of 3: {is_power(63, 3)}')
    print(f'9 is the power of 3: {is_power(9, 3)}')
