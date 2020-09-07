s = 'elangbrely'

largo = len(s)
aux = ['']*largo
M = 0
cont = 0 
L = 0
    
while M < largo - 1:
    
    while s[L] <= s[L+1] and L < largo-2:
        cont += 1
        L += 1
    if L == largo-2 and s[L] <= s[L+1]:
        aux[M] = s[L-cont:L+2]
    else:
        aux[M] = s[L-cont:L+1]
    cont = 0
    L += 1
    M = L

largo_max = [0]*largo

for i in range(0,largo):
    largo_max[i] = len(aux[i])
    
pos = largo_max.index(max(largo_max))
print "Longest substring in alphabetical order is: ",aux[pos]
print aux







