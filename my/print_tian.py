#! python3
# print_tian.py - Prints a image of 田 like
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

# Requirement:
# Has flexible magnitude
# The cross of lines is a plus sign.

def print_plus():
    """Prints a '+' ending with a space"""
    print('+', end=' ')

def print_minus():
    """Prints a '-' ending with a space"""
    print('-', end=' ')

def print_bar():
    """Prints a '|' ending with a space"""
    print('|', end=' ')

def print_pm_line(arg):
    """Prints a line with plus and minus signs.
    
    arg: The length of a kou 
    """
    print_plus()
    minus_num = int(arg / 2)
    for i in range(minus_num):
        print_minus()
    print_plus()
    for i in range(minus_num):
        print_minus()
    print('+')

def print_bar_line(arg):
    """Prints a line with spaces and bars
    
    arg: The length of a kou
    """
    print_bar()
    space_num = int(arg / 2)
    for i in range(space_num):
        print('  ', end='')
    print_bar()
    for i in range(space_num):
        print('  ', end='')
    print('|')

while True: 
    print('Please input the length of kou:')
    kou_len_str = input()
    kou_len = int(kou_len_str)
    if isinstance(kou_len, int) is False:
        print('Please input a integer. ')
        continue
    if int(kou_len) < 3:
        print('Please the length of kou should large than or equal 3')
        continue
    if int(kou_len)%2 == 0:
        print('Please input a odd number.')
        continue
    break

print('Please input the height of kou:')
kou_h_str = input()
kou_h = int(kou_h_str)

print_pm_line(kou_len)
for i in range(kou_h):
    print_bar_line(kou_len)
print_pm_line(kou_len)
for i in range(kou_h):
    print_bar_line(kou_len)
print_pm_line(kou_len)
