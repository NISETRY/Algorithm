import pprint
from collections import deque
N, M, K = map(int, input().split())

graph = [[0]* M for _ in range(N)]
q = deque()
for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            graph[i][j] = 1
            # print(graph)
# pprint.pprint(graph)
visited = [[0] * M for _ in range(N)]
count = []
for r in range(N):
    for c in range(M):
        if graph[r][c] == 0 and visited[r][c] == 0:
            q.append((r,c))
            visited[r][c] = 1
            cnt = 1
            while q:
                cur_r, cur_c = q.popleft()

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr = cur_r + dr
                    nc = cur_c + dc 
                    if 0<=nr<N and 0<=nc<M and graph[nr][nc] == 0 and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        cnt += 1
                        q.append((nr, nc))
            count.append(cnt)
count.sort()
print(len(count)) 
print(*count)
