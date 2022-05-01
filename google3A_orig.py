def solution(n):
    n = int(n)
    i = 0
    while(n>1):
        i = i + 1
        if n % 2 == 0:
            n = n/2
        elif n % 4 == 3:
            n = n+1
        else:
            n = n-1
    return i