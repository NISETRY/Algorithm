n,m=map(int,input().split())
res=[]
def nHm(x):
    if len(res)==m:
        print(*res)
        return
    for i in range(x,n+1):
        res.append(i)
        nHm(x)
        res.pop()
nHm(1)