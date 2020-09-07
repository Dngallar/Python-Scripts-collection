# python 2
#CONVERSION AND COMPRESSION

# Domingo Gallardo Saavedra

def numToBaseB( N, B ):
  if N == 0:
    return ''
  for i in range(B):
    if N%B == i:
        return  numToBaseB(N/B,B) + str(i)
        
def baseBToNum(S, B):
  if S == '':
    return 0
  s_num = int(S)
  s_str_aux = str(s_num)
  largo = len(s_str_aux)
  Num = 0
  for i in range(largo):
      Num += int(s_str_aux[i])*(B**(largo-1-i))
  return Num
  
def baseToBase(B1,B2,s_in_B1):
    num_B1 = baseBToNum(s_in_B1, B1)
    return numToBaseB(num_B1, B2 )
    
def add(S,T):
    """ add two binary number"""
    s_num = baseBToNum(S, 2)
    t_num = baseBToNum(T, 2)
    return numToBaseB( s_num + t_num, 2 )
    
def addB(S,T):
    """ Suma binaria sin funcion convertir"""
    if len(S) < len(T):
        S = '0'*(len(T)-len(S)) + S
    if len(S) > len(T):
        T = '0'*(len(S)-len(T)) + T
        
    s_bin = [int(i) for i in S]
    t_bin = [int(i) for i in T]
    largo = len(s_bin)
    
    suma = [s_bin[i]+t_bin[i] for i in range(largo)]
    suma = [0] + suma
    
    for i in range(2):
        for t in range(largo+1):
            if suma[largo-t] == 2:
                suma[largo-t-1] = suma[largo-t-1] + 1
                suma[largo-t] = 0
            elif suma[largo-t] == 3:
                suma[largo-t-1] = suma[largo-t-1] + 1
                suma[largo-t] = 1        
    
    suma_str = ''
    for i in range(largo+1):
        suma_str += str(suma[i])
    
    return str(int(suma_str))
    
def compress(S):
    gradi = '' #*len(S)
    for i in range(len(S)-1):
        gradi += gradiente(S[i:i+2])
    try:
        num_patt = gradi.count('+') + 1
    except:
        num_patt = 1
        
    pos = [-1]+[-1]*num_patt
    for i in range(num_patt):
        pos[i+1] = gradi.find('+',pos[i]+1)+1
    if S[0] == '0':      
        pos = [0] + pos[1:-1] + [len(S)]
    elif S[0] == '1':      
        pos = [1] + pos[1:-1] + [len(S)]
    
    pos_aux = [pos[i] for i in range(len(pos))]
        
    for i in range(1,len(pos)-1):
        pos[i+1] = pos_aux[i+1] - pos_aux[i]
        
    bit7_pos = [binToBinary7Bit(numToBaseB(pos[i],2)) for i in range(1,len(pos))]
    
    if num_patt%2 == 0:
        comp = ['']*2*num_patt
    else:
        comp = ['']*2*(num_patt+1)
    
    
    
    for i in range((num_patt+1)/2):
        if S[0] == '0':
            comp[4*i] = '0'
            comp[2*(i+2**i)] = '1'
        if S[0] == '1':
            comp[4*i] = '1'
            comp[2*(i+2**i)] = '0'
    
    if num_patt%2 == 0:
        comp = comp
    else:
        comp = comp[0:-2]
    
    for i in range(num_patt):
        comp[2*i+1] = bit7_pos[i]
    
    comp_final = ''
    for i in range(num_patt*2):
        comp_final += comp[i]
        
    return comp_final
    
def gradiente(S):
    if S[0] == '0' and S[1] == '1':
        return '+'
    elif S[0] == '1' and S[1] == '0':
        return '+'
    else:
        return '0'
            
def binToBinary7Bit(num):
    if len(num) < 7:
        num = '0'*(7-len(num))+num
    return num
         
    
def uncompress(C):
    num_patt = len(C)/8
    list_patt = [C[8*i:8*i+8] for i in range(num_patt)]
    cant = [baseBToNum(list_patt[i][1:],2) for i in range(num_patt)]
    valor = [list_patt[i][0] for i in range(num_patt)] 
    uncomp = ''
    for i in range(num_patt):
        uncomp += str(valor[i])*cant[i] 
        
    return uncomp
        
    