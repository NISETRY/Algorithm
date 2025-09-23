from collections import deque

def dfs(s):
    if len(picked) == M:
        print(*picked)

    for i in range(s, N+1):
        picked.append(i)
        dfs(i+1)
        picked.pop()
    


picked = deque()
N, M = map(int, input().split())

dfs(1)