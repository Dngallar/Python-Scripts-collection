#python 2

# Domingo Gallardo Saavedra

import random
import math

def dartThrow():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0) 
    
    if x**2 + y**2 <= 1:
        return True
    else:
        return False
        
def forPi( n ):
    numhits = 0
    numthrows = 0
    
    for i in range(n):
        numthrows += 1
        if dartThrow():
            numhits += 1
        pi = 4.0*numhits/numthrows
        print numhits, 'hits out of',numthrows,'throws so that pi is', pi
    return pi    

def whilePi( maxerror ):
    n = 1
    numhits = 0
    numthrows = 1
    
    if dartThrow():
        numhits += 1
        
    estpi = 4.0*numhits/numthrows
    print numhits, 'hits out of',numthrows,'throws so that pi is', estpi
       
    while abs(math.pi - estpi) >= maxerror:
        for i in range(n):
            numthrows += 1
            if dartThrow():
                numhits += 1
        estpi = 4.0*numhits/numthrows
        print numhits, 'hits out of',numthrows,'throws so that pi is', estpi
    return numthrows