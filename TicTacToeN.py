# TIC-TAC-TOE + N
#
# Name:Domingo Gallardo Saavedra
#

# here is a function for printing 2d arrays
# (lists-of-lists) of data

def print2d( A ):
    """ print2d prints a 2d array, A
        as rows and columns
        input: A, a 2d list of lists
        output: None (no return value)
    """
    NR = len(A)
    NC = len(A[0])

    for r in range(NR): # NR = =numrows
        for c in range(NC):  # NC == numcols
            print A[r][c],
        print

    return None  # this is implied anyway,
    # when no return statement is present

# create a 2d array from a 1d string
def createA( NR, NC, s ):
    """ returns a 2d array with
        NR rows (numrows) and
        NC cols (numcols)
        using the data from s: across the
        first row, then the second, etc.
        We'll only test it with enough data!
    """
    A = []
    for r in range(NR):
        newrow = []
        for c in range(NC):
            newrow += [ s[0] ] # add that char
            s = s[1:]   # get rid of that first char
        A += [newrow]
    return A
    
def inarow_3east( ch, r, c, A ):
    w = len(A[0])
    
    if w - c < 3 or A[r][c] != ch:
        return False
    elif A[r][c] == ch and A[r][c+1] == ch and A[r][c+2] == ch: 
        return True
    else:
        return False
        
        
def inarow_3south( ch, r, c, A ):
    h = len(A)
    
    if h - r < 3 or A[r][c] != ch:
        return False
    elif A[r][c] == ch and A[r+1][c] == ch and A[r+2][c] == ch: 
        return True
    else:
        return False
        
def inarow_3se( ch, r, c, A ):
    h = len(A)
    w = len(A[0])
    
    if h - r < 3 or w - c < 3 or A[r][c] != ch:
        return False
    elif A[r][c] == ch and A[r+1][c+1] == ch and A[r+2][c+2] == ch: 
        return True
    else:
        return False
        
def inarow_3ne( ch, r, c, A ):
    w = len(A[0])
    
    if r < 2 or w - c < 3 or A[r][c] != ch:
        return False
    elif A[r][c] == ch and A[r-1][c+1] == ch and A[r-2][c+2] == ch: 
        return True
    else:
        return False
    
def inarow_Neast( ch, r, c, A, N ):
    w = len(A[0])
    
    if w - c < N or A[r][c] != ch:
        return False
    else:
        aux = True
        for i in range(N):
            aux *= (A[r][c+i] == ch)
        if aux:
            return True
        else:
            return False
    
def inarow_Nsouth( ch, r, c, A, N ):
    h = len(A)
    
    if h - r < N or A[r][c] != ch:
        return False
    else:
        aux = True
        for i in range(N):
            aux *= (A[r+i][c] == ch)
        if aux:
            return True
        else:
            return False
        
def inarow_Nse( ch, r, c, A, N ):
    h = len(A)
    w = len(A[0])
    
    if h - r < N or w - c < N or A[r][c] != ch:
        return False
    else:
        aux = True
        for i in range(N):
            aux *= (A[r+i][c+i] == ch)
        if aux:
            return True
        else:
            return False
        
def inarow_Nne( ch, r, c, A, N ):
    w = len(A[0])
    
    if r < N-1 or w - c < N or A[r][c] != ch:
        return False
    else:
        aux = True
        for i in range(N):
            aux *= (A[r-i][c+i] == ch)
        if aux:
            return True
        else:
            return False
        
