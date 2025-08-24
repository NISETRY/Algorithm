import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
turn = 0
def dfs(node):
    global count
    
    for i in grid[node]:
        if not visited[i] :
            count += 1
            visited[i] = count
            dfs(i)
    return 

N, M, R = map(int, input().split())
grid = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    start, end = map(int, input().split())
    grid[start].append(end)
    grid[end].append(start)

# sort
for i in range(len(grid)):
    grid[i].sort()

count = 1
visited[R] = count
dfs(R)
for i in range(1, len(visited)):
    print(visited[i])