import sys
sys.setrecursionlimit(1000000)

n=int(input())
# 상하좌우
dr=[0,0,-1,1]
dc=[-1,1,0,0]
res=-1
flag=True
bamboo=[list(map(int,input().split())) for _ in range(n)]
dp=[[1]*n for _ in range(n)]

def dfs(r,c,d,dist):
    if d==0 and dp[r][c]!=1:
        return dp[r][c]
    if d==4:
        return 1
    nr,nc=r+dr[d],c+dc[d]
    cur=bamboo[r][c]
    best=0
    if 0<=nr<n and 0<=nc<n and bamboo[nr][nc]>cur:
        best=max(best, 1+dfs(nr,nc,0,1))
    best=max(best,dfs(r,c,d+1,dist))
    if d==0:
        dp[r][c]=best
    return best

for i in range(n):
    if flag:
        for j in range(n):
            tmp=dfs(i,j,0,1)
            res=max(res,tmp)
            if tmp==n**2:
                flag=False
                break
print(res)