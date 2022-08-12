#! python3
# do_four.py - Print a statement four times.

# Requirement:
# Def a function using two parameters, one parameter is a function,
# one parameter is a value that will be printed. 
# The defined function take two statements as its body

def print_something(arg):
    """Prints the arg.
    
    arg: anything can be printed. 
    """
    print(arg)

def do_twice(fun, arg):
    """Runs a function twice.
    
    fun: function object
    arg: argument passed to the function
    """
    fun(arg)
    fun(arg)

def do_four(f, v):
    """Runs a function four times.
    
    f: function object
    v: argument passed to the function
    """
    do_twice(f, v)
    do_twice(f, v)

do_four(print_something, 'spams')