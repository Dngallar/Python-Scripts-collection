# python 2
#
# Homework 3, Problem 3
# List comprehensions!
#
# Name:Domingo Gallardo Saavedra
#

# this gives us functions like sin and cos
from math import *

# two more functions (not in the math library above)
def dbl(x):
    """ doubler!  input: x, a number """
    return 2*x

def sq(x):
    """ squarer!  input: x, a number """
    return x**2

# examples for getting used to list comprehensions
def lc_mult( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each multiplied by 2**
    """
    return [ 2*x for x in range(N) ]

def lc_idiv( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each divided by 2**
        WARNING: this is INTEGER division...!
    """
    return [ float(x/2) for x in range(N) ]

def lc_fdiv( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each divided by 2**
        NOTE: this is floating-point division...!
    """
    return [ float(x)/2 for x in range(N) ]


# Here is where your functions start for the homework:

# Step 1, part 1
def unitfracs( N ):
    """ Example: >>> unitfracs(2)
        [0.0, 0.5]
    """
    return [ float(x)/N for x in range(N) ]

def scaledfracs(low, hi, N):
    """ Example: scaledfracs( 10, 30, 5 )
        [10.0, 14.0, 18.0, 22.0, 26.0]
    """
    return [ low+float(hi-low)*x/N for x in range(N) ]

def sqfracs(low,hi,N):
    """ Example: >>> sqfracs(4,10,6)
       [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
    """
    return [ x**2 for x in scaledfracs(low,hi,N)]

def f_of_fracs(f,low,hi,N):
    """ Examples:
        >>> f_of_fracs(dbl, 10, 20, 5)
        [20.0, 24.0, 28.0, 32.0, 36.0]
        >>> f_of_fracs(sq, 4, 10, 6)
        [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
    """
    return [ f(x) for x in scaledfracs(low,hi,N)]

def integrate(f,low,hi,N):
    """ integrate returns an estimate of the definite integral
     of the function f (the first input)
     with lower limit low (the second input)
     and upper limit hi (the third input)
     where N steps are taken (the fourth input)

    integrate simply returns the sum of the areas of rectangles
    under f, drawn at the left endpoints of N uniform steps
    from low to hi
    """
    y = f_of_fracs(f,low,hi,N)
    width = (hi-1.0*low)/N
    return sum(y)*width