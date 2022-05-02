def solution( l , t ):
    s = sum(l)
    if s == t:
        return [0, (len(l)-1) ]
    for k in range(0,len(l),1):
        parsum = 0
        for i in range( k, len(l), 1 ):
            parsum = parsum + l[i]
            if parsum == t:
                return [k,i]
    return [-1, -1]