from itertools import combinations
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def bfs():
    q = deque()
    visited = [[2*(N-1)+1] *N for _ in range(N)]
    
    # 시작점 큐에 추가
    for store_idx in store_idx_set:
        r, c = store_rcs[store_idx]
        visited[r][c] = 0
        q.append((r, c))
        
    while q:
        r, c = q.popleft()
        
        for dir in range(4):
            nr, nc = r+dr[dir], c+dc[dir]
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if visited[nr][nc] <= visited[r][c] + 1:
                continue
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))
    distance = 0
    for r,c in home_rcs:
        distance += visited[r][c]
        
    return distance

N, M = map(int,input().split())

graph = [[0] * N for _ in range(N)]

home_rcs = []
store_rcs = []
answer = float('inf')

for r in range(N):
    row = list(map(int,input().split()))

    for c in range(N):
        graph[r][c] = row[c]

        if graph[r][c] == 1:
            home_rcs.append((r,c))
        elif graph[r][c] == 2:
            store_rcs.append((r,c))


for store_idx_set in combinations(range(len(store_rcs)) , M):
    answer = min(answer, bfs())
print(answer)