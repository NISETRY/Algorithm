def bfs():
    que = fire
    
    while que:
        x,y = que.pop(0)
        if x>=0 and y>=0:
            if graph[x][y] == 0:
                return visited[x][y]
            
            for dx,dy in move:
                nx, ny = dx+x, dy+y
                
                if 0<=nx<n+2 and 0<=ny<m+2:
                    if visited[nx][ny] == 0 and (graph[nx][ny] == '.' or graph[nx][ny] == 0):
                        que.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
                
        else:
            for dx,dy in move:
                nx, ny = dx-x, dy-y
                
                if 0<=nx<n+2 and 0<=ny<m+2:
                    if visited[nx][ny] == 1 and (graph[nx][ny] == '.' or graph[nx][ny] == 0):
                        que.append((-nx,-ny))
                        visited[nx][ny] = 1

    return 'IMPOSSIBLE'

n, m = map(int, input().split())
graph = [[0]*(m+2) for _ in range(n+2)]
visited = [[0]*(m+2) for _ in range(n+2)]
move = [[-1,0],[0,1],[1,0],[0,-1]]
fire = []

for i in range(n):
    temp = list(input())
    for j in range(m):
        graph[i+1][j+1] = temp[j]


for x in range(n+2):
    for y in range(m+2):
        if graph[x][y] == 'F':
            fire.append((-x,-y))
            visited[x][y] = 1

        if graph[x][y] == 'J':
            fire.append((x,y))
            visited[x][y] = 1

ans = bfs()
print(ans-1)