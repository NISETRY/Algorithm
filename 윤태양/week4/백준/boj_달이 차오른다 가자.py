from collections import deque

def bfs(a,b):
    global visited
    que = deque([(a,b,0,0)]) # 큐에 key 들고다니고, key 얻으면 visited 변화
    visited[0][a][b] = 1       # 그러면 방문횟수도 들고다녀야겠네
                           
    while que:
        x,y,cnt,key = que.popleft()
        if graph[x][y] == '1':
            return cnt
        
        for dx, dy in move:
            nx,ny = dx+x, dy+y

            if 0<=nx<n and 0<=ny<m:
                if visited[key][nx][ny] == 0 and graph[nx][ny] in can_go:
                    visited[key][nx][ny] = 1
                    que.append((nx,ny,cnt+1,key))

                elif visited[key][nx][ny] == 0 and graph[nx][ny] in keys:
                    new_key = key | 1 << (ord(graph[nx][ny]) - ord('a')) 
                    visited[new_key][nx][ny] = 1
                    que.append((nx,ny,cnt+1,new_key))
                    
                elif visited[key][nx][ny] == 0 and graph[nx][ny] in door:
                    if key & 1 << (ord(graph[nx][ny]) - ord('A')):
                        visited[key][nx][ny] = 1
                        que.append((nx,ny,cnt+1,key))
    return -1

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[[0]*m for _ in range(n)] for _ in range(64)]
move = [[-1,0],[1,0],[0,1],[0,-1]]

can_go = ['0','.','1']
keys = ['a','b','c','d','e','f']
door = ['A','B','C','D','E','F']

for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            print(bfs(i,j))
