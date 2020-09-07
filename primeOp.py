i = 2
def is_Prime(n):
    global i
    if i == n-1:
        i = 2
        return True
    elif n == 1:
        return False
    elif n == 2:
        return True
    elif n%i == 0:
        i = 2
        return False
    else:
        i += 1
        return is_Prime(n)

def addPrimes(L):
    global suma
    if len(L) == 0:
        suma = 0
        return 0
    else:
        if is_Prime(L[0]):
            return L[0] + addPrimes(L[1:])
        else:
            return addPrimes(L[1:])
        
        