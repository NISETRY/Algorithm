from collections import deque

def bfs(a,b):
    visited = [[0]*m for _ in range(n)]
    visited[a][b] = 1
    que = deque([(a,b)])

    while que:
        x, y = que.popleft()

        for dx, dy in move:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    que.append((nx,ny))
                    visited[nx][ny] = 1
                    if counter[nx][ny] == 0:
                        counter[nx][ny] = counter[x][y] + 1
                                        
                    else:
                        counter[nx][ny] = min(counter[x][y]+1, counter[nx][ny])

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
counter = [[0]*m for _ in range(n)]
move = [[-1,0],[0,1],[0,-1],[1,0]]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i,j)
cnt = 0
tomato_wall = 0
ans = -1

for r in range(n):
    for c in range(m):
       ans = max(ans, counter[r][c])
       if graph[r][c] == 1 or graph[r][c] == -1:
           tomato_wall += 1
       if counter[r][c] == 0:
           cnt += 1

if cnt == tomato_wall:
    print(ans)

else:
    print(-1)
