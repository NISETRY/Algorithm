from itertools import combinations

N, M = map(int, input().split())

graph = [[0] * N for _ in range(N)]

home_rcs = []
store_rcs = []
answer = float('inf')

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        graph[r][c] = row[c]

        if graph[r][c] == 1:
            home_rcs.append((r, c))
        elif graph[r][c] == 2:
            store_rcs.append((r, c))

distances = [[0] * len(store_rcs) for _ in range(len(home_rcs))]

for home_idx in range(len(home_rcs)):
    for store_idx in range(len(store_rcs)):
        distances[home_idx][store_idx] = abs(home_rcs[home_idx][0] - store_rcs[store_idx][0]) + abs(home_rcs[home_idx][1] - store_rcs[store_idx][1])

# list(combinations(range(len(store_rcs)), M)) 쓰지 말것 X
for store_idx_set in combinations(range(len(store_rcs)), M):

    distance = 0
    for home_idx in range(len(home_rcs)):
        min_distance = 2*(N-1)
        for store_idx in store_idx_set:
            min_distance = min(min_distance, distances[home_idx][store_idx])

        distance += min_distance
    
    answer = min(answer, distance)

print(answer)


########2 dfs
from itertools import combinations
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque()
    visited = [[2*(N-1)+1]*N for _ in range(N)]
    
    for store_idx in store_idx_set:
        r, c = store_rcs[store_idx]
        visited[r][c] = 0
        q.append((r, c))
    
    while q:
        r, c = q.popleft()
        
        for dir in range(4):
            nr = r+dr[dir]
            nc = c+dc[dir]
            
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if visited[nr][nc] <= visited[r][c]+1:
                continue

            visited[nr][nc] = visited[r][c]+1
            q.append((nr, nc))
    
    distance = 0
    for r, c in home_rcs:
        distance += visited[r][c]

    return distance
    

N, M = map(int, input().split())
graph = [[0]*N for _ in range(N)]

home_rcs = []
store_rcs = []
answer = float('inf')

for r in range(N):
    rcs = list(map(int, input().split()))
    for c in range(N):
        graph[r][c] = rcs[c]
        if graph[r][c] == 1:
            home_rcs.append((r, c))
        elif graph[r][c] == 2:
            store_rcs.append((r, c))

for store_idx_set in combinations(range(len(store_rcs)), M):
    
    answer = min(answer, bfs())

print(answer)

