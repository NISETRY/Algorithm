from collections import deque
from copy import deepcopy

def bfs(a,b):
    global graph
    que = deque([(a,b)])

    while que:
        x,y = que.popleft()
        
        for dx,dy in move:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<n:
                if og_graph[nx][ny] == graph[nx][ny]:
                    graph[nx][ny] = graph[nx][ny] + graph[x][y]
                    que.append((nx,ny))
                    continue

                if graph[x][y] + og_graph[nx][ny] < graph[nx][ny]:
                    graph[nx][ny] = graph[x][y] + og_graph[nx][ny]
                    que.append((nx,ny))

t = int(input())

for tc in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    og_graph = deepcopy(graph)
    move = [[0,1],[1,0]]
    bfs(0,0)
    
    print(f'#{tc+1} {graph[n-1][n-1]}')