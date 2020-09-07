def genPrimes():
    prim = [2]
    yield 2
    while True:
        cont = 0
        next = prim[-1] + 1
        for i in prim:
            if (next%i) != 0:
                cont += 1
        if cont == len(prim):
            yield next
        prim += [next]
    
            
        