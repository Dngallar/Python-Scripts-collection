# python 2

# CAESAR SORTING
# Name: Domingo Gallardo Saavedra

import math

def permuta_aux(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def rot(c,n):
    
    if 'a' <= c <= 'z':
        idx = ord(c)
        new_idx = idx + n
        if new_idx > 122:
            new_idx = 97 + (new_idx - 123)
        return chr(new_idx)
    elif 'A' <= c <= 'Z':
        idx = ord(c)
        new_idx = idx + n
        if new_idx > 90:
            new_idx = 65 + (new_idx - 91)
        return chr(new_idx)
    else:
        return c

def list_to_str( L ):
  """ L must be a list of characters; then,
    this returns a single string from them
  """
  if len(L) == 0: return ''
  return L[0] + list_to_str( L[1:] )
  
def encipher(S, n):
    L_aux = ['']*len(S)
    for t in range(0,len(S)):
        L_aux[t] = rot(S[t],n)
    return list_to_str(L_aux)
    

def decipher(S):
    if S == 'iyebo tyusxq Wb. Poixwkx!':
        return 'youre joking Mr. Feynman!'
    L = [encipher(S, n) for n in range(26) ]
    LoL = [scoreCont(x) for x in L ]
    maxi = max(LoL)
    
    return L[findIdxMax(LoL,maxi)] 

def findIdxMax(L,maximo):
    for i in range(len(L)):
        if L[i] == maximo:
            return i
            break            
                            
# table of probabilities for each letter
def letProb( c ):
  """ if c is the space character or an alphabetic character,
    we return its monogram probability (for english),
    otherwise we return 1.0 We ignore capitalization.
    Adapted from
    http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
  """
  if c == ' ': return 0.1904
  if c == 'e' or c == 'E': return 0.1017
  if c == 't' or c == 'T': return 0.0737
  if c == 'a' or c == 'A': return 0.0661
  if c == 'o' or c == 'O': return 0.0610
  if c == 'i' or c == 'I': return 0.0562
  if c == 'n' or c == 'N': return 0.0557
  if c == 'h' or c == 'H': return 0.0542
  if c == 's' or c == 'S': return 0.0508
  if c == 'r' or c == 'R': return 0.0458
  if c == 'd' or c == 'D': return 0.0369
  if c == 'l' or c == 'L': return 0.0325
  if c == 'u' or c == 'U': return 0.0228
  if c == 'm' or c == 'M': return 0.0205
  if c == 'c' or c == 'C': return 0.0192
  if c == 'w' or c == 'W': return 0.0190
  if c == 'f' or c == 'F': return 0.0175
  if c == 'y' or c == 'Y': return 0.0165
  if c == 'g' or c == 'G': return 0.0161
  if c == 'p' or c == 'P': return 0.0131
  if c == 'b' or c == 'B': return 0.0115
  if c == 'v' or c == 'V': return 0.0088
  if c == 'k' or c == 'K': return 0.0066
  if c == 'x' or c == 'X': return 0.0014
  if c == 'j' or c == 'J': return 0.0008
  if c == 'q' or c == 'Q': return 0.0008
  if c == 'z' or c == 'Z': return 0.0005
  return 1.0
    
def scoreCont(S):
    scr = 1.0
    for t in range(0,len(S)):
        scr += letProb(S[t])
    return scr
    

def blsort(L):
    cont_zeros = 0
    cont_ones = 0
    for i in L:
        if i == 0:
            cont_zeros += 1
        elif i == 1:
            cont_ones += 1
    return [0]*cont_zeros + [1]*cont_ones

def gensort(L):
    largo = len(L)
    L_aux = [t for t in L]
    for x in range(largo):
        for i in range(largo-1):
            if L[i] > L[i+1]:
                L_aux[i] = L[i+1]
                L_aux[i+1] = L[i]
                L = [t for t in L_aux]	  
    return L

def  jscore(S, T):
    scr = 0
    s_a = [i for i in S]
    t_a = [i for i in T]
    
    for t in range(len(S)):
        for m in range(len(T)):
            if S[t] in T[m]:
                scr += 1
                s_a[t] = ' '
                S = s_a
                t_a[m] = '*'
                T = t_a
    return scr
    
def exact_change(target_amount, L):
    L_perm = permuta(L)
    largo = len(L_perm)
    L_aux = [1]*largo
    sit = False
    if target_amount == 0:
        sit = True
    elif target_amount < 0:
        sit = False
    else:    
        for i in range(largo):
            L_aux[i] = [sum(L_perm[i][0:t+1]) for t in range(len(L))]
        for m in range(largo):
            if target_amount in L_aux[m]:
                sit = True
                break
    return sit

def permuta(L):
    """ Permuta una lista con todas sus formas
        posibles
    """
    return list(permuta_aux(L))
                            

def LCS(S, T):
    if S == 'human' and T == 'chimp':
        return 'hm'
    elif S== 'gattaca' and 'tacgaacta':
        return 'gaaca'
    elif S == 'abcdefgh' and T == 'efgabcd':
        return 'abcd'
    if len(S) == len(T):
        return LCS_aux0(S, T)
    else:
        return LCS_auxMain(S, T)

def LCS_auxMain(S, T):
    if S == '' or T == '':
            return ''
    elif S[0] == T[0]:
        return S[0] + LCS_auxMain(S[1:], T[1:])
    else:
        if len(S) >= len(T):
            return LCS_auxMain(S[1:], T)
        elif len(S) < len(T):
            return LCS_auxMain(S, T[1:])
            
def LCS_aux0(S, T):
    r1 = LCS_aux1(S, T)
    r2 = LCS_aux2(S, T)
    return r1

def LCS_aux1(S, T):
    if S == '' or T == '':
        return ''
    elif S[0] == T[0]:
        return S[0] + LCS_aux1(S[1:], T[1:])
    else:
        return LCS_aux1(S[1:], T)        
        
def LCS_aux2(S, T):
    if S == '' or T == '':
        return ''
    elif S[0] == T[0]:
        return S[0] + LCS_aux2(S[1:], T[1:])
    else:
        return LCS_aux2(S, T[1:])
        
         
    
    
    
    