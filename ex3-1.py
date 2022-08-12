#! python3
# ex3-1.py - Print a name at the end of a line.
# The final character of the name should be in the column of this line.

# Need: 
# the name of the function is right_justify
# the parameter name input is 's'

def right_justify(s):
    name_len = len(s)
    print(" " * (70 - name_len), end='')
    print(s)

a = input()
right_justify(a)
