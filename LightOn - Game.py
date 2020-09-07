# python 2
#
# Homework 4, Problem 1
# "Lights On!"
#
# Name: Domingo Gallardo Saavedra
#
#

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.


def mutate(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = 1 + oldL[i]
    return new_ith_element


def evolve(oldL, curgen = 0):
    """ This function should evolve oldL (a list)
        it starts at curgen, the "current" generation
        and it ends at generation #5 (for now)
        
        It works by calling mutate at each index i.
    """
    print oldL,                    # print the old list, L
    print ""
    #time.sleep(0.25)
    largo = len(oldL)
    L_aux = range(0,largo)
    if allOnes(oldL):
        print curgen 
        return curgen    # no return value... yet
    else:
        user = choice(L_aux)
        newL = [ mutate6(i,oldL,user) for i in range(len(oldL)) ]
        return evolve(newL, curgen + 1)

def mutate0(i, oldL):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    new_ith_element = 2 * oldL[i]
    return new_ith_element

def mutate1(i, oldL):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    new_ith_element = oldL[i]**2
    return new_ith_element
    
def mutate2(i, oldL):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    new_ith_element = oldL[i-1]
    return new_ith_element
    
def mutate3(i, oldL):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    new_ith_element = choice([0, 1])
    return new_ith_element

def mutate4(i, oldL, user=0):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    if i == user:
        new_ith_element = 1        # this makes the game easy!
    else:
        new_ith_element = oldL[i] # the new is the same as the old
    return new_ith_element
    
    
def mutate5(i, oldL, user=0):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    if i == user:
        if oldL[i] == 0:
            new_ith_element = 1
            
        elif oldL[i] == 1:
            new_ith_element = 0
    else:
        new_ith_element = oldL[i]
            
    return new_ith_element
    
    
def mutate6(i, oldL, user=0):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    if i == user or i == user + 1 or i == user - 1 and user != 0:
        if oldL[i] == 0:
            new_ith_element = 1
                    
        elif oldL[i] == 1:
            new_ith_element = 0
            
    else:
        new_ith_element = oldL[i]
            
    return new_ith_element
               
def allOnes(L):
    if len(L) == 0:
        return True
    else:
        d = 1
        for i in L:
            d *= i
        if d == 1: return True
        else: return False
        
def randBL(N):
    if N == 2:
        L = choice ([[0,0],[1,1]]) #This because when N =2 there is a bug
    else:
        L = [0]*N
        for t in range(0, N):
            L[t] = choice([0,1])
    return L

evolve(randBL(3))
