import sys
input=sys.stdin.readline

n,m=map(int,input().split())
pick=[]

def nCm(x):
    if len(pick)==m:
        print(*pick)
        return
    for i in range(x,n+1):
        if i not in pick:
            pick.append(i)
            nCm(i+1)
            pick.pop()

nCm(1)