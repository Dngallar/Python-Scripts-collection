def tpl(x):
    """ output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return 3*x
    
def sq(x):
    """ output: sq retur the square of its input
        input x: a number
    """
    return x**2
    
def interp(low,hi,fraction):
    """ output: return the floating-point value 
        that is fraction of the way between low and hi.    
        input: 3 numbers low, hi and fraction
    """
    if fraction == 0:
        return low
    elif fraction == 1:
        return hi
    else:
        return fraction*(hi-low) + low
        
def checkends(s):
    """ Takes in a string s and returns True if the first 
        character in s is the same as the last character in s.
        It returns False otherwise.
    """
    if len(s) == 0 or s[0] == s[-1]:
        return True
    else:
        return False
        
def flipside(s):
    """ takes in a string s and returns a string whose first
        half is s's second half and whose second half is s's 
        first half
    """
    x = len(s)/2
    return s[x::] + s[0:x]
    
def convertFromSeconds(s):
    """ takes in a nonnegative integer number of seconds s and 
        returns a list (we'll call it L) of four nonnegative integers
        that represents that number of seconds in more conventional units
        of time
    """
    days = s / (24*60*60)
    s = s % (24*60*60)
    hours = s/(60*60)
    s = s % (60*60)
    minutes = s/60
    s = s % (60)
    seconds = s
    return [days, hours, minutes, seconds]
    
def front3(str):
    """ Given a string, we'll say that the front is the first 3 chars 
        of the string. If the string length is less than 3, the front 
        is whatever is there. Return a new string which is 3 copies o
        f the front. 
    """
    if len(str) < 3:
        return str*3
    else:
        return str[0:3]*3
    
    
    
    
    
    
    
    
    
    
    
    
    
    