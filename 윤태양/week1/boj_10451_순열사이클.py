import sys
t = int(sys.stdin.readline())

def bfs(a):
    visited[a] = 1
    que = [a]

    while que:
        x = que.pop(0)
        if not visited[graph[x]]:
            que.append(graph[x])
            visited[graph[x]] = 1

for i in range(t):

    n = int(sys.stdin.readline())
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0]*(n+1)
    ans = 0

    for i in range(1, n+1):                        
        if visited[i] == 0:                    
            bfs(i)
            ans+=1

    print(ans)
