import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, adj, block=None):
    """start에서 adj를 따라 BFS. block이 주어지면 그 정점은 통과 금지(미리 방문 처리)."""
    n = len(adj) - 1
    vis = [False] * (n + 1)
    if block is not None:
        vis[block] = True
    q = deque([start])
    vis[start] = True
    while q:
        x = q.popleft()
        for y in adj[x]:
            if not vis[y]:
                vis[y] = True
                q.append(y)
    return vis


n, m = map(int, input().split())
g  = [[] for _ in range(n+1)]  # 정방향
gr = [[] for _ in range(n+1)]  # 역방향
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    gr[b].append(a)
S, T = map(int, input().split())

# 1) S에서 도달 가능한 정점 (T는 중간 금지)
fromS = bfs(S, g, block=T)
# 2) T에서 도달 가능한 정점 (S는 중간 금지)
fromT = bfs(T, g, block=S)
# 3) S에 도달 가능한 정점(= 역방향에서 S에서 갈 수 있는 정점)
toS   = bfs(S, gr, block=None)
# 4) T에 도달 가능한 정점(= 역방향에서 T에서 갈 수 있는 정점)
toT   = bfs(T, gr, block=None)

ans = 0
for v in range(1, n+1):
    if v == S or v == T:
        continue
    if fromS[v] and fromT[v] and toS[v] and toT[v]:
        ans += 1
print(ans)


