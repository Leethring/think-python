# Estimate the square root of a
# by using Newton's method
# y = (x + a/x) / 2
# x = y

a = 4
x = 1
precision = 0.00001

while True:
    print(x)
    y = (x + a/x) / 2
    if abs(x - y) < precision:
        break
    x = y