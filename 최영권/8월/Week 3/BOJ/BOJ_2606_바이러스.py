computers = int(input())
pair = int(input())
lst = [] 
graph = [[] for _ in range(computers+1)]
visited = [False] * (computers+1)

def virus(a, grid, visited):
   
    if visited[a] == False:
        visited[a] = True

    global lst
    lst.append(a)
    
    for i in range(len(grid[a])):
        if not visited[grid[a][i]]:
            virus(grid[a][i], grid, visited)


for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

virus(1, graph, visited)
print(len(lst)-1)
