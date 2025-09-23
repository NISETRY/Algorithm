from collections import deque
from itertools import combinations
import pprint
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

virus = []
empty = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty.append((i,j))
        if arr[i][j] == 2:
            virus.append((i,j))

def spread(graph, virus):
    q = deque(virus)
    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if graph[nr][nc] == 0:
                graph[nr][nc] = 2
                q.append((nr, nc))

max_safe = 0
for walls in combinations(empty, 3):
    tmp = [row[:] for row in arr]

    for r, c in walls:
        tmp[r][c] = 1

    spread(tmp, virus)
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1

    max_safe = max(max_safe, cnt)
print(max_safe)