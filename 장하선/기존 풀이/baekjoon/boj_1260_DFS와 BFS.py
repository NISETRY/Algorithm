n,m,v=map(int, input().split())
spots=[[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    spots[a][b]=spots[b][a]=1

visited_dfs=[]
visited_bfs=[]

def dfs(start):
    visited_dfs.append(start)
    for i in range(1,n+1):
        if spots[start][i]==1 and i not in visited_dfs:
            dfs(i)
    return visited_dfs

def bfs(start):
    visited_bfs.append(start)
    queue=[start]
    while queue:
        x=queue.pop(0)
        for i in range(1,n+1):
            if spots[x][i]==1 and i not in visited_bfs:
                visited_bfs.append(i)
                queue.append(i)
    return visited_bfs

print(*dfs(v))
print(*bfs(v))