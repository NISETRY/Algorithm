from collections import deque

def bfs():
    while que:
        x, y = que.popleft()

        for dx, dy in move:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    que.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
move = [[-1,0],[0,1],[0,-1],[1,0]]
que = deque()
ans = -1
flag = False

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append((i,j))
            visited[i][j] = 1

        elif graph[i][j] == -1:
            visited[i][j] = -1
bfs()

for r in visited:
    if flag:
        break
    for c in r:
        if c == 0:
            ans = 0
            flag = True
            break

        else:
            ans = max(ans, c)

print(ans-1)
