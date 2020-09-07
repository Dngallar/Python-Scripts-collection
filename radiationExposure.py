def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    d = int((stop-start)/step)
    
    x_axi = [start]*d
    
    for i in range(1,d):
        x_axi[i] = x_axi[i-1] + step  
    
    y_axi = [f(i) for i in x_axi]
    
    return step*sum(y_axi)