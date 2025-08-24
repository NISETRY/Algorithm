from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
visited = [[[0,0] for _ in range(m)] for _ in range(n)]
move = [[-1,0],[1,0],[0,1],[0,-1]]

def bfs(a,b):
    visited[a][b][0] = 1
    que = deque([(a,b,0)])

    while que:
        x,y,broken = que.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][broken]

        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny][broken] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    que.append((nx,ny,broken))

                elif visited[nx][ny][0] == 0 and graph[nx][ny] == 1 and broken == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    que.append((nx,ny,1))

    return -1

ans = bfs(0,0)
print(ans)