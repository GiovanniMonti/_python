def solution(L):
    L.sort(reverse=True)
    rem = sum(L) % 3
    j = ''
    remlist1 = []
    remlist2 = []
    if rem == 0 :
        for i in L:
            j = j + str(i)
        return int(j)

    for i in range(-1, -len(L)-1,-1):
        if L[i]%3 == 1:
            remlist1.append(L[i])
        elif L[i]%3 == 2:
            remlist2.append(L[i])

    if rem == 1:
        if len(remlist1) > 0:
            L.remove(remlist1[0])
        elif len(remlist2) > 1:
            L.remove(remlist2[0])
            L.remove(remlist2[1])
    if rem == 2:
        if len(remlist2) > 0:
            L.remove(remlist2[0])
        elif len(remlist1) > 1:
            L.remove(remlist1[0])
            L.remove(remlist1[1])
    
    rem = sum(L) % 3
    if rem == 0 and not len(L) == 0:
        for i in L:
            j = j + str(i)
        return int(j) 
    return 0

print( solution( [4] ) )