from collections import deque

N, M = map(int, input().split())


picked = deque()

def dfs(s):
    if len(picked) == M:
        print(*picked)

    for i in range(s, N+1):
        if i not in picked:
            picked.append(i)
            dfs(s)
            picked.pop()


dfs(1)