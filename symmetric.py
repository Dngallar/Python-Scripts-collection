def symmetric(S):
    h = len(S)
    ST = []    
    for i in range(h):
        ST.append([0]*h)
    for i in range(h):
        for j in range(h):
            ST[j][i] = S[i][j]
    if ST == S:
        return True
    else:
        return False