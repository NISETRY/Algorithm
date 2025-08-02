n,m=map(int,input().split())
res=[]
def nCm(x):
    if len(res)==m:
        print(*res)
        return
    for i in range(x,n+1):
        if i not in res:
            res.append(i)
            nCm(i+1)
            res.pop()
nCm(1)