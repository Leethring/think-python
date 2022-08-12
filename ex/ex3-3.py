#! python3
# ex3-3.py - Prints a 田, like
#
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +

def print_pm():
    """Prints a line of plus and minus"""
    print('+', '- '*4 + '+', '- '*4 + '+')

def print_bar():
    """Prints three bars with 9 space"""
    print('|' + ' '*9 + '|' + ' '*9 + '|')

print_pm()
for i in range(4):
    print_bar() 
print_pm()
for i in range(4):
    print_bar() 
print_pm()