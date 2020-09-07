def isOdd(n):
    if n%2 == 0:
        return False
    else:
        return True
        
def numToBinary(N):
  if N == 0:
    return ''
  elif N%2 == 1:
    return  numToBinary(N/2) + '1'
  else:
    return  numToBinary(N/2) + '0'
    
def binaryToNum(S):
  if S == '':
    return 0
  s_num = int(S)
  s_str_aux = str(s_num)
  largo = len(s_str_aux)
  Num = 0
  for i in range(largo):
      Num += int(s_str_aux[i])*(2**(largo-1-i))
  return Num
  
def increment(S):
    largo = len(S)
    num = binaryToNum(S) + 1
    numBin = numToBinary(num)
    largo_aux = len(str(numBin))
    largo_zeros = largo - largo_aux
    if largo_aux > largo:
        return '0'*largo
    return '0'*largo_zeros + numBin
    
def increment8bit(S):
    largo = 8
    num = binaryToNum(S) + 1
    numBin = numToBinary(num)
    largo_aux = len(str(numBin))
    largo_zeros = largo - largo_aux
    return '0'*largo_zeros + numBin

def count(S, n):
    print S
    for i in range(n):
        num = increment8bit(numToBinary(binaryToNum(S)+i))
        print num[-8:]
        
def numToTernary(N):
  if N == 0:
    return ''
  elif N%3 == 2:
    return  numToTernary(N/3) + '2'
  elif N%3 == 1:
    return  numToTernary(N/3) + '1'
  else:
    return  numToTernary(N/3) + '0'
    
def ternaryToNum(S):
  if S == '':
    return 0
  s_num = int(S)
  s_str_aux = str(s_num)
  largo = len(s_str_aux)
  Num = 0
  for i in range(largo):
      Num += int(s_str_aux[i])*(3**(largo-1-i))
  return Num
  
  
def balancedTernaryToNum(S):
  if S == '':
    return 0
  largo = len(S)
  Num = [0]*largo
  New_str = [0]*largo
  for i in range(largo):
      New_str[i] = changeSymbols(S[i])
      
  for i in range(largo):
      Num[i] += int(New_str[i])*(3**(largo-1-i))
  return sum(Num)
  
def changeSymbols(c):
    if c == '-': return -1
    if c == '+': return 1
    if c == '0': return 0
    
def numToBalancedTernary(N):
  if N == 0:
    return ''
  elif N%3 == 2:
    return  numToBalancedTernary((N+3)/3) + '-'
  elif N%3 == 1:
    return  numToBalancedTernary(N/3) + '+'
  else:
    return  numToBalancedTernary(N/3) + '0'