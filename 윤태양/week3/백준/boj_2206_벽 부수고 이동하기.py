from collections import deque

def bfs(a,b):
    visited[a][b] = 1
    que = deque([(a,b,0)])
    
    while que:
        x, y, cnt = que.popleft()
        cnt += 1
        if x == n-1 and y == m-1:
            break
        for dx, dy in move:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    que.append((nx,ny,cnt))
                    visited[nx][ny] = 1
     
                    
    if x == n-1 and y == m-1:
        return cnt
    else:
        return -1
    

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
wall = 0
wall_idx = []
move = [[-1,0],[0,1],[0,-1],[1,0]]

for r in range(n):
    for c in range(m):
        if graph[r][c] == 1:
            wall += 1
            wall_idx.append((r,c))

ans = 9999
for i, j in wall_idx:
    visited = [[0]*m for _ in range(n)]
    graph[i][j] = 0
    bfs_return = bfs(0,0)
    
    if bfs_return != -1:
        if bfs_return<=ans:
            ans = bfs_return
            
    graph[i][j] = 1
    

if ans == 9999:
    print(-1)
else:
    print(ans)
    
    
# 시간 개선 아이디어 
# 한 번의 bfs를 돌 때, 벽 부수기 까지 해서 딱 한 번만 bfs 돌고도 답을 찾을 수 있게 함
# 그러면 재귀로 해야하나?