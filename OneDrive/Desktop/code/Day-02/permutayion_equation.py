def permutationEquation(p):
    n = len(p)
    res=[]
    for x in range(1, n + 1):
        k = p.index(x) + 1
        j = p.index(k)
        res.append(j+1)
    return res