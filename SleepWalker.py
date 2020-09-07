# python 2
#
# Homework 3, Problem 2
#
# Name: Domingo Gallardo Saavedra
#

import random  

def rs():
    """ rs chooses a random step and returns it 
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])

def rwpos(start, nsteps):
    """ This function return the 
        random walker's position.
    """
    #print 'start is', start
    if nsteps == 0:
        #print start
        return start
    else:
        start = start + rs()
        return rwpos(start, nsteps-1)
    

num_steps = 0
def rwsteps(start, low, hi):
    """simulate a random walk, printing each step"""
    global num_steps
    if start == low or start == hi:
        print " "*(start-low-1)+"S"+" "*(low-start-1)
        print num_steps     
        return num_steps
    else:
        num_steps += 1
        print " "*(start-low-1)+"S"+" "*(low-start-1)
        start = rwpos(start,1)
        start = rwsteps(start, low, hi)
        
   
def rwposPlain(start, nsteps):
    """ This function return the 
        random walker's position.
    """
    if nsteps == 0:
        return start
    else:
        start = start + rs()
        return rwposPlain(start, nsteps-1)    
    

def ave_signed_displacement(numtrials):
    suma = 0
    LC = [rwposPlain(0,100) for x in range(numtrials)]
    for x in range(numtrials):
        suma += LC[x]
    return round(suma/float(numtrials),2)

def ave_squared_displacement(numtrials):
    suma = 0
    LC = [rwposPlain(0,100) for x in range(numtrials)]
    for x in range(numtrials):
        suma += LC[x]**2
    return round(suma/float(numtrials),2)
        
"""
   In order to compute the average signed displacement for
   a random walker after 100 random steps, I 
     (briefly explain what you did and your results)

   Be sure to copy the data and average from at least
   one of your runs of ave_signed_displacement and
   at least one of your runs of ave_squared_displacement
"""