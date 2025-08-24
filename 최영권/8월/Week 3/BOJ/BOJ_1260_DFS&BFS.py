from collections import deque
def dfs(graph, v):
    visited = []
    stack = [v]
    while stack:
        d = stack.popleft()
        if d not in visited:
            visited.append(d)
            stack += reversed(graph[d])




















N, M, V = map(int, input().split())


arr = [[] for _ in range(N)]   # 인접 리스트 생성
for i in range(M):
    start, end = map(int, input().split())
    arr[start-1].append(end)
    arr[start-1].sort()



