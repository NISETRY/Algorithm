import sys

n, l = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(l):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(num):
    visited[num] = 1
    que = [num]
    
    while que:
        x = que.pop(0)
        
        for i in graph[x]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = 1
cnt = 0
for i in range(1, n+1):
    if visited[i] ==0:
        bfs(i)
        cnt+=1
print(cnt)