import sys
input=sys.stdin.readline

n,m=map(int,input().split())
pick=[]

def nPm():
    if len(pick)==m:
        print(*pick)
        return
    for i in range(1,n+1):
        if i not in pick:
            pick.append(i)
            nPm()
            pick.pop()

nPm()