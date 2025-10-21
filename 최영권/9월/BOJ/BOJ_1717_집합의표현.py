N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
def dfs(num, idx):
    if b in graph[num]:
        return 'YES'
    for i in range(len(graph[a])):
        print(graph[a])
        print(graph[a][i])
        dfs(graph[a][i], i+1)

    return 'NO'
for _ in range(M):
    oper, a, b = map(int, input().split())
    if oper == 0:
        if b not in graph[a]:
            graph[a].append(b)
            graph[b].append(a)

    elif oper == 1:
        dfs(a, 0)