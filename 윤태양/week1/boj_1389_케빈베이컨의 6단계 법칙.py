n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(q):
    visited[q] = 1
    que = [q]

    while que:
        a = que.pop(0)
        
        for i in graph[a]:
            if visited[i] == 0:
                cost[i] = cost[a]+1
                visited[i] = 1
                que.append(i)

    return sum(cost)

ans = []

for i in range(1, n+1):
    cost = [0 for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    ans.append(bfs(i))

print(ans.index(min(ans))+1)
