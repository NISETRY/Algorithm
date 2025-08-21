def bfs(x,y):
    global counter
    visited = [[0]*m for _ in range(n)]
    counter = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    counter[x][y] = 1
    que = [(x,y)]

    while que:
        a, b = que.pop(0)
        
        for dx,dy in move:
            nx,ny = a+dx, b+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] != -1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    graph[nx][ny] = 1
                    que.append((nx,ny))
                    if counter[nx][ny] == 0:
                        counter[nx][ny] = counter[a][b] + 1
                        continue

                    if counter[a][b] + 1 < counter[nx][ny]:
                        counter[nx][ny] = counter[a][b] + 1

    answer = -1
    for i in range(n):
        for j in range(m):
            answer = max(answer, counter[i][j])
    return answer 
              
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [[-1,0],[1,0],[0,1],[0,-1]]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans = bfs(i,j)
            ans -= 1


for r in range(n):
    for c in range(m):
        if graph[r][c] == 0:
            ans = -1

print(ans)
print(counter)