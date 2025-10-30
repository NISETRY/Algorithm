def comb(count, idx):
    global answer 

    if count == m:
        visited = [[0]*n for _ in range(n)]
        time2 = bfs(pick, visited)
        answer = min(answer, time2)
        return
    
    else:
        for i in range(n):
            if i>idx:
                pick.append(i)
                comb(count+1, i)
                pick.pop()
# BFS
def bfs(pick, visited):
    time = 0
    que = deque(pick)
    for p in que:
        visited[p[0]][p[1]] = 1

    while que:
        x,y = que.popleft()
        
        for dx,dy in move:
            nx,ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] != 1 and visited[nx][ny] == 0:        
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx,ny))
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] > time:
                time = visited[i][j]
    
    return time

from collections import deque

                

# 기본 세팅
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [(-1,0),(1,0),(0,1),(0,-1)]
virus = []
pick = []
answer = 9999999


# 바이러스 위치
for i in range(n):        
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i,j))


