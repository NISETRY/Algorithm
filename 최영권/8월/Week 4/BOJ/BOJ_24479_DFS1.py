N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)   
answer = [0] * (N+1)
count = 1
stack = [R]
visited[R] = True
answer[R] = count
while stack:
    u = stack.pop()
    
    for v in reversed(graph[u]):
        if visited[v] == False:
            visited[v] = True
            count += 1
            answer[v] = count
            stack.append(v)

for i in range(1, len(answer)):
    print(answer[i])