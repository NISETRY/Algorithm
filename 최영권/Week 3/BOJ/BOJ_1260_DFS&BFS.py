from collections import deque
n, m, v = map(int, input().split())
arr = [[] * (n+1) for _ in range(n+1)]

for i in range(m):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)
    arr[start].sort()
    arr[end].sort()

visited_1 = [False] * (n+1)
dfs_answer = []
def dfs(graph, v, visited):
    if visited_1[v] == False:
        visited_1[v] = True
    
    global dfs_answer
    dfs_answer.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited_2 = [False] * (n+1)
bfs_answer = []

def bfs(graph, v, visited):
    q = deque([v])

    if visited_2[v] == False:
        visited_2[v] = True

    global bfs_visited
    while q:
        i = q.popleft()
        bfs_answer.append(i)

        for j in graph[i]:
            if not visited_2[j]:
                q.append(j)
                visited_2[j] = True

dfs(arr, v, visited_1)
print(*dfs_answer)


bfs(arr, v, visited_2)
print(*bfs_answer)