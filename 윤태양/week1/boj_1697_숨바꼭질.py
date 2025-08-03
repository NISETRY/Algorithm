n, k = map(int, input().split())
visited = []
graph = []

def act(n):
    move1 = 2*n
    move2 = n+1
    move3 = n-1
    return [move1, move2, move3]

def bfs(n):
    visited.append(n)
    que = [n]
    graph.append([n])
    a = n
    
    while a!=k:
        a = que.pop(0)
        move = act(a)
        
        for i in move:
            if a not in visited:
                graph.append([i])
                que.append(i)
                visited.append(i)
                
            elif a in visited:
                for i in graph:
                    try:
                        idx = i.index(a)
                    except:
                        pass
                graph[idx].append(i)
                que.append(i)
                visited.append(i)
bfs(n)
print(graph)
                        
        
        