# SWEA 5248 그룹 나누기 - DFS 풀이
import sys
input = sys.stdin.readline

def dfs(start, visited, graph):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for nxt in graph[node]:
                if not visited[nxt]:
                    stack.append(nxt)

T = int(input().strip())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))

    # 인접리스트 생성
    graph = [[] for _ in range(N+1)]
    for i in range(0, 2*M, 2):
        a, b = info[i], info[i+1]
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N+1)
    groups = 0

    # 모든 사람을 돌면서 DFS
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i, visited, graph)
            groups += 1

    print(f"#{tc} {groups}")
