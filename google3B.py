def solution(x, y):
    M, F = max(int(x), int(y)),min(int(x), int(y))
    r = 0
    while(F>0):
        r +=M//F
        M,F = F,M%F
    if M != 1:
        return 'impossible'
    return str(r-1)