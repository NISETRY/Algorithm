from collections import deque

def bfs(a,b):
    visited[a][b][0] = 1
    que = deque([(a,b,0)])

    while que:
        x,y,br = que.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][br]
        

        for dx,dy in move:
            nx, ny = x+dx, y+dy
            
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny][br] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny][br] = visited[x][y][br] + 1
                    que.append((nx,ny,br))

                elif  graph[nx][ny] == 1 and br <k and visited[nx][ny][br+1] == 0:
                    visited[nx][ny][br+1] = visited[x][y][br] + 1
                    que.append((nx,ny,br+1))

    return -1
                    

n,m,k = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
move = [[-1,0],[1,0],[0,1],[0,-1]]

print(bfs(0,0))