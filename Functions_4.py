# python 2
#
# Homework 8, Problem 1
# Loops!
#
# Name: Domingo Gallardo Saavedra
#


import random

def fac(n):
    """ loop-based factorial function 
        input: a nonnegative integer n
        output: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

# tests: run by pressing the Run button above

print "fac(0): should be 1 == ", fac(0)
print "fac(5): should be 120 == ", fac(5)


def power(b,p):
    result = 1
    for i in range (p):
        result = result*b
    return result
    
print "power(2,5): should be 32 == ", power(2,5)
print "power(5,2): should be 25 == ", power(5,2)
print "power(42,0): should be 1 == ", power(42,0)
print "power(0,42): should be 0 == ", power(0,42)
print "power(0,0): should be 1 == ", power(0,0)

def summedOdds( L ):
    """ loop-based function to return a numeric list, summed
        (sum is built-in, so we're using a different name)
        input: L, a list of integers
        output: the sum of the list L
    """
    result = 0
    for e in L:
        if e%2 != 0:
            result = result + e  # or result += e
    return result

# tests!
print "summedOdds( [4,5,6] ): should be 5 == ", summedOdds( [4,5,6] )
print "summedOdds( range(3,10) ): should be 24 == ", summedOdds( range(3,10) )



def untilARepeat( high ):
    
    L = []
    cont = 0
    while uniq(L):
        L = L + [random.choice( range(0,high) )]
        cont += 1  
    return cont

def uniq( L ):
    """ returns whether all elements in L are unique
        input: L, a list of any elements
        output: True, if all elements in L are unique,
             or False, if there is any repeated element
    """
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return uniq( L[1:] ) # recursion is OK, too!
