#Maximo Comun Divisor

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    L_a = [i for i in range(1,a+1) if a%i == 0]
    L_b = [i for i in range(1,b+1) if b%i == 0]
    L_eq = [i for i in L_a if i in L_b]
    
    return max(L_eq)