import sys
input=sys.stdin.readline

n=int(input())
cnt=0
col=[0]*n;diag=[0]*(2*n-1);adiag=[0]*(2*n-1);check=[0]*n

def queen(r):
    global cnt
    if r==n:
        cnt+=1
        return
    for c in range(n):
        d=r-c+n-1
        a=r+c
        if not col[c] and not diag[d] and not adiag[a]:
            check[r]=c
            col[c]=diag[d]=adiag[a]=1
            queen(r+1)
            col[c]=diag[d]=adiag[a]=0

queen(0)
print(cnt)