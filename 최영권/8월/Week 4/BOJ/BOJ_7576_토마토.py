from collections import deque
M, N = map(int, input().split())

d = [(1,0), (-1,0), (0,1),(0,-1)]
# BFS
# 1위치 q에 담기
# q길이 만큼 4방향 탐색하여 
# 0인곳을 1로 바꾸고
# day += 1

graph = []
q = deque()
for r in range(N):
    temp = list(map(int, input().split()))
    for c in range(len(temp)):
        if temp[c] == 1:
            q.append((r, c))
    graph.append(temp)

def bfs(que):
    day = -1
    while que:
        for _ in range(len(que)):
            sr, sc = que.popleft()

            for dr, dc in d:
                nr = sr + dr
                nc = sc + dc
                if 0<=nr<N and 0<=nc<M and graph[nr][nc] == 0:
                    graph[nr][nc] = 1
                    q.append((nr,nc))
        day += 1
    for r in graph:
        for c in r:
            if c == 0:
                day = -1
                break
    
    return day

print(bfs(q))