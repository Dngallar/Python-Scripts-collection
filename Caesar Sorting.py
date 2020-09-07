# python 2

# CAESAR SORTING
# Name: Domingo Gallardo Saavedra

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
    

    
    
    
    
    