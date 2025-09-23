from itertools import combinations
from collections import deque
N, M = map(int, input().split())
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)
arr = [list(input()) for _ in range(N)]
land = deque()

    
def bfs(r, c):
    dist = 0
    q = deque()
    q.append((r, c))
    visited = [[-1]*M for _ in range(N)]
    visited[r][c] = 0
    while q:
        r, c = q.popleft()
        d = visited[r][c]
        dist = max(d, dist)
        
        for dir in range(4):
            nr, nc = r+dr[dir], c+dc[dir]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 'L' and visited[nr][nc] == -1:
                visited[nr][nc] = d + 1
                q.append((nr, nc))
    return dist
answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            answer = max(answer, bfs(i, j))
print(answer)