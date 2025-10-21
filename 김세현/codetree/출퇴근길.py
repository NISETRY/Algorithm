from collections import deque
import sys
input = sys.stdin.readline

# 정방향 bfs
def bfs_forward_until(start, stop, graph, n):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()

        # 도착점에 도착하면 해당 노드에서 더 이상 이어지는 간선을 탐색하지 않음
        if cur == stop:
            continue

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return visited

# 역방향 bfs: 중단 없이 전체 탐색
def bfs_full(start, graph, n):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return visited

# 입력
n, m = map(int, input().split())
g  = [[] for _ in range(n + 1)]  # 정방향 그래프
gr = [[] for _ in range(n + 1)]  # 역방향 그래프

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    gr[v].append(u)

S, T = map(int, input().split())

# 출근길: S->v, v->T
go_S = bfs_forward_until(S, T, g, n)
to_T = bfs_full(T, gr, n)

# 퇴근길: T->v, v->S
go_T = bfs_forward_until(T, S, g, n)
to_S = bfs_full(S, gr, n)

# 출발/도착 제외 + 출근/퇴근 모두 만족하는 정점 개수
ans = 0
for i in range(1, n + 1):
    # 출발점, 도착점 제외
    if i == S or i == T:
        continue
    if go_S[i] and to_T[i] and go_T[i] and to_S[i]:
        ans += 1

print(ans)