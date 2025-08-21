def bfs(x,y):
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    que = [(x,y)]

    while que:
        x,y = que.pop(0)
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx,ny))
    answer = -1 
    for i in range(n):
        for j in range(m):
            if visited[i][j] > answer:
                answer = visited[i][j]

    return answer

n, m = map(int, input().split())
temp = [list(input()) for _ in range(n)]
graph = [[0]*m for _ in range(n)]
move = [[-1,0],[0,1],[0,-1],[1,0]]
ans = -1 

for r in range(n):
    for c in range(m):
        if temp[r][c] == 'W':
            graph[r][c] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            temp = bfs(i,j)
            ans = max(temp, ans)

print(ans-1)
