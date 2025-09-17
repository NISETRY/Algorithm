import sys
input=sys.stdin.readline

n,m=map(int,input().split())
pick=[]

def nHm(x):
    if len(pick)==m:
        print(*pick)
        return
    for i in range(x,n+1):
        pick.append(i)
        nHm(i)
        pick.pop()

nHm(1)