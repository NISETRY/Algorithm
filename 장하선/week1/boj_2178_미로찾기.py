from collections import deque
n,m=map(int,input().split())
maze=[[] for _ in range(n)]
visited = [[False]*m for _ in range(n)]
visited[0][0]=True
queue=deque([(0,0)])
for i in range(n):
    k=input()
    for j in range(m):
        maze[i].append(int(k[j]))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if maze[nx][ny]!=0 and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny]=True
                    maze[nx][ny]=maze[x][y]+1
print(maze[n-1][m-1])