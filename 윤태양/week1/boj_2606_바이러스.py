n = int(input())
l = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(l):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(num):
    visited[num] = 1
    que = [num]
    cnt = 0
    
    while que:
        x = que.pop(0)
        
        for i in graph[x]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = 1
                cnt+=1
    return cnt

print(bfs(1))