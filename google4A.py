from itertools import combinations


def solution(num_buns, num_required):
    res = [[] for _ in range(num_buns)]
    x = num_buns - num_required + 1
    for k,b in enumerate( combinations(range(num_buns),x) ):
        for bny in b:
            res[bny].append(k)
    return res

print( solution( 2,1 ) )