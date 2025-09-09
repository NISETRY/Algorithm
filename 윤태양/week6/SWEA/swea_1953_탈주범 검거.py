from collections import deque
import pprint

def bfs(r,c):
    visited[r][c] = 1
    que = deque([(r,c)])
    area = 0 

    while que:
        x,y = que.popleft()
        delta = move[graph[x][y]]
        area += 1
        print(x,y)

        for dx,dy in delta:
            nx,ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0 and graph[nx][ny] != 0:
                    for moved in move[graph[nx][ny]]:
                        if [-moved[0],-moved[1]] in move[graph[x][y]]:
                                if visited[x][y] + 1 <= l and visited[nx][ny] == 0:
                                    visited[nx][ny] = visited[x][y] + 1
                                    que.append((nx,ny))
    return area
                    

t = int(input())

for tc in range(t):
    n,m,r,c,l = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
            # 상하좌우   # r = 상하 # c = 좌우
    move =  [[[0]],[[-1,0],[1,0],[0,-1],[0,1]], [[-1,0],[1,0]], [[0,-1],[0,1]], 
              [[1,0],[0,1]],[[-1,0],[0,1]],[[-1,0],[0,-1]],[[1,0],[0,-1]]]

    print(f'#{tc+1} {bfs(r,c)}')
