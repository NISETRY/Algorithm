def bfs(r,c):
    visited[r][c] = 1
    que = [(r,c)]
    
    while que:
        x, y = que.pop(0)
        if graph[x][y] == 3:
            return visited[x][y] - 2
        
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] != 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx,ny))
    return 0

t= int(input())
for tc in range(t):
    n = int(input())
    
    graph = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    move = [[-1,0],[0,1],[1,0],[0,-1]]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                ans = bfs(i,j)

    print(f'#{tc+1} {ans}')
