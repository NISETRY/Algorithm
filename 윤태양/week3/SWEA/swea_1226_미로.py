def bfs(r,c):
    visited[r][c] = 1
    que = [(r,c)]

    while que:
        x, y = que.pop(0)
        if graph[x][y] == 3:
            return 1

        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0<=nx<16 and 0<=ny<16:
                if graph[nx][ny] != 1 and visited[nx][ny] != 1:
                    visited[nx][ny] = 1
                    que.append((nx,ny))
    return 0

for tc in range(10):
    input()
    
    graph = [list(map(int, list(input()))) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    move = [[-1,0],[0,1],[1,0],[0,-1]]

    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                ans = bfs(i,j)

    print(f'#{tc+1} {ans}')
