n=int(input())
dan=[list(input().strip()) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dan[i][j]=='0':
            visited[i][j]=1
num_dan=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x,y,dir,tmp):
    visited[x][y]=1
    tmp+=1
    for dir in range(4):
        nx,ny=x+dx[dir],y+dy[dir]
        if 0<=nx<n and 0<=ny<n and dan[nx][ny]=='1' and not visited[nx][ny]:
            tmp=dfs(nx,ny,0,tmp)
    return tmp

for i in range(n):
    for j in range(n):
        if dan[i][j]=='1' and not visited[i][j]:
            num_dan.append(dfs(i,j,0,0))

num_dan.sort()
k=len(num_dan)
print(k)
for x in num_dan:
    print(x)