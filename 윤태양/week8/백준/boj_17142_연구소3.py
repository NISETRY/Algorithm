# 0, 1, 2는 빈칸, 벽, 바이러스
# 퍼져나가는 로직 = bfs
# 선택 로직 = 조합
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [[-1,0],[1,0],[0,1],[0,-1]]
virus = []
temp = []
answer = 999999

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i,j))

def bfs(que):
    que = que
    visited = [[0]*n for _ in range(n)]
    
    for r,c in que:
        visited[r][c] = 1
    # que = deque([(r,c)])

    while que:
        x,y = que.popleft()
        
        for dx, dy in move:
            nx,ny = dx+x, dy+y
            
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1 
                    que.append((nx,ny))

                elif visited[nx][ny] == 0 and graph[nx][ny] == 2:
                    visited[nx][ny] = 1
                    que.append((nx,ny))
    
    for_return = 0
    for r in range(n):
        for c in range(n):
            for_return = max(visited[r][c], for_return)
    print(visited)

    return for_return


def comb(count, idx):
    global answer 

    if count == m:
        que = deque()
        for i in temp:
            r,c = virus[i]
            que.append(r,c)
            bfs(que)
            answer = min(now, answer)
        return
    
    for i in range(1, len(virus)):
        if i > idx:
            temp.append(i)
            comb(count+1, i)
            temp.pop()

comb(0,0)

print(answer-1)


# 바이러스는 이미 감염됐으므로, 추가로 감염 시킬 필요가 없음 -> 로직 추가