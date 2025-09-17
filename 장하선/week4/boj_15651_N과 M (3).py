import sys
input=sys.stdin.readline

n,m=map(int,input().split())
pick=[]

def nPIm():
    if len(pick)==m:
        print(*pick)
        return
    for i in range(1,n+1):
        pick.append(i)
        nPIm()
        pick.pop()

nPIm()