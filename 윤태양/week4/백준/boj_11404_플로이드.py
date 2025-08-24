def dfs(s,e,c, visited):
    if s==e:
        return c
    
    visited[s] = 1
    min_cost = 9999999999999
    
    for nx in range(len(graph[s])):
        if visited[nx] == 0 and graph[s][nx] != 9999999999999:
            new_cost = c + graph[s][nx]
            result = dfs(nx,e,new_cost,visited)
            min_cost = min(min_cost, result)

    visited[s] = 0

    return min_cost
    

n = int(input())
m = int(input())

graph = [[9999999999999]*n for _ in range(n)]
answer = [[0]*n for _ in range(n)]


for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        
        visited = [0]*n
        answer[i][j] = dfs(i,j,0,visited)
        
        if answer[i][j] >=9999999999999:
            answer[i][j] = 0

for i in answer:
    print(*i)