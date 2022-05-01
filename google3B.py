def solution(M,F):
    i = 0
    M = int(M)
    F = int(F)
    m=1
    f=1
    while(m != M and f != M):
        i = i + 1

        if M-m < F-f:
            m = m + f
        elif M-m > F-f:
            f = m + f
        else:
            return 'impossible'
    return i

solution('2', '1')