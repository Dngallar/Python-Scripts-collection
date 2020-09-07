# Domingo Gallardo Saavedra - 02/07/2015

def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))
    
def merge(left, right):
    global contInv
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
            
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result
    
 
import random
lista = [0]*50000
for i in range(50000):
    lista[i] = random.randint(1,50000000)
from time import time  
start_time = time()
listaOrdenada = merge_sort(lista)
elapsed_time = time() - start_time
print elapsed_time