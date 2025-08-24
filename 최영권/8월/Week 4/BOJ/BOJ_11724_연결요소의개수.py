import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int, input().split()) 
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = [0] * (N+1)
count = 0
def dfs(n):
    q = deque([n])
    visited[n] = 1
    while q:
        node = q.pop()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append(nxt)
    

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)