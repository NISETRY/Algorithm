from collections import deque
from pprint import pprint

n, m = map(int, input().split()) # 연구소 사이즈, 활성 가능 바이러수 수
graph = [list(map(int, input().split())) for _ in range(n)] # 연구소
move = [(-1,0),(1,0),(0,1),(0,-1)]
answer = 9999

virus = []
temp = []
pick = []

for r in range(n):
    for c in range(n):
        if graph[r][c] == 2:
            virus.append((r,c))  # 바이러스 찾아서, 위치 추가

def comb(count, idx):
    global answer
    
    if count == m:
        pick = temp[:]
        cnt = bfs(pick)
        if cnt is not None:
            answer = min(cnt, answer)
        return 
    
    for i in range(len(virus)):
        if i > idx:
            temp.append(virus[i])
            comb(count+1, i)
            temp.pop()
            
            
def bfs(que):
    que = deque(que)
    visited = [[-1]*n for _ in range(n)]
    
    for r,c in que:
        visited[r][c] = 0
        
    while que:
        x,y = que.popleft()
        
        for dx,dy in move:
            nx,ny = dx+x, dy+y
            
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1 and graph[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx,ny))
                    
    count = -1
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and visited[i][j] == -1:
                return None
            if graph[i][j] == 0:
                count = max(visited[i][j], count)
            
    return count

room = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            room += 1    


comb(0,-1)

if room == 0:
    answer = 0
    
if answer == 9999:
    print(-1)
else:
    print(answer)