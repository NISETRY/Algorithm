n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = graph[n2][n1] = 1
    
visited = [0]*(n+1)

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            visited[i] = 1
            dfs(i)
dfs(v)
print()

visited = [0]*(n+1)
que = [v]

def bfs(v):
    visited[v] = 1

    while que:
        v = que.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] == 0 and graph[v][i] == 1:
                que.append(i)
                visited[i] = 1
        
bfs(v)  # 풀이 1


# n, m, v = map(int, input().split())

# graph = [[0]*(n+1) for _ in range(n+1)]

# for _ in range(m):
#     n1, n2 = map(int, input().split())
#     graph[n1][n2] = graph[n2][n1] = 1
    
# visited = [0]*(n+1)

# def dfs(v):
#     visited[v] = 1
#     print(v, end=' ')
    
#     for i in range(1, n+1):
#         if visited[i] == 0 and graph[v][i] == 1:
#             visited[i] = 1
#             dfs(i)
# dfs(v)
# print()

# visited = [0]*(n+1)
# que = [v]

# def bfs(v):
#     visited[v] = 1

#     while que:
#         v = que.pop(0)
#         print(v, end=' ')
#         for i in range(1, n+1):
#             if visited[i] == 0 and graph[v][i] == 1:
#                 que.append(i)
#                 visited[i] = 1
        
# bfs(v)  # 풀이 2