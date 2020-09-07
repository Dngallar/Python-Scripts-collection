def uniquify(L):
    if len(L) == 0:
        return []
    else:
        if L[0] not in L[1:]:
            return [L[0]] + uniquify(L[1:])
        else:
            return uniquify(L[1:])