from collections import deque

N, M = map(int, input().split())

# 인접리스트 만들기
lst = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = -1
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

def dfs(start, cnt):
    q = deque()
    global result
    visited[start] = True

    if start == u:
        result = cnt
        return

    for i in lst[start]:
        if visited[i] == False:
            dfs(i, cnt+1)
            if result != -1:
                return

dfs(1, cnt)
print(cnt)
