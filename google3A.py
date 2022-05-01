#       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
rems = [0,1,0,1,0,1,0,1,0,1,0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

def solution(n):
    i = 0
    l = []
    l[:0] = n.strip()
    while( int(l[0]) > 1 or len(l) > 1 ):
        curl = len(l)
        i = i + 1

        if rems[int(l[curl-1] )] == 0:
            l = dividelist(l)
        elif int(l[curl-2] + l[curl-1]) % 4 == 3 and curl > 1:
            addtoList(l)
        else:
            l[curl-1] = str( int( l[curl-1] ) - 1 )
        #print(i,l)
        
    return i

def addtoList(n):
    n[len(n)-1] = str( int( n[len(n)-1]) + 1)    
    for i in range(-1,-len(n),-1):
        if int(n[i]) > 9: #case increase digit count ignored
            n[i] = str( 0 )
            n[i-1] = str( int(n[i-1]) + 1 )


def dividelist(n):
    nstr = []
    rem = 0
    for i in n:
        if rems[int( i ) + (rem* 10) ] == 0 :
            nstr.append( str( (int( (int( i ) + (rem* 10) )) )>>1 ))
            rem = 0
        else:
            nstr.append( str( int( (int( i ) + (rem* 10) -1 ))>>1 ))
            rem = rems[int( i ) + (rem* 10)]
    while(nstr[0] == '0'):
        nstr.remove(nstr[0])
    return nstr

print( solution( '768 ' ) )