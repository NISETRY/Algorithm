from collections import deque

def bfs():
    while que:
        z,x,y = que.popleft()

        for dx,dy,dz in move:
            nx,ny,nz = x+dx,y+dy,z+dz
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    que.append((nz,nx,ny))

m,n,h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0]*m for _ in range(n)] for _ in range(h)]
move = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]

que = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):    
            if graph[k][i][j] == 1:
                que.append((k,i,j))
                visited[k][i][j] = 1

            elif graph[k][i][j] == -1:
                visited[k][i][j] = -1

bfs()
ans = 1
flag = False
for z in range(h):
    for x in range(n):
        for y in range(m):
            ans = max(ans, visited[z][x][y])
            if visited[z][x][y] == 0:
                flag = True
if flag:
    print(-1)
else:
    print(ans-1)
