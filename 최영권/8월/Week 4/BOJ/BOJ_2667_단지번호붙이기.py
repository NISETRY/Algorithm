dist = [(1,0),(-1,0),(0,1),(0,-1)]
N = int(input())
visit = [[False] * N for _ in range(N)]
def dfs(graph, sr, sc, visited):
    global count
    visited[sr][sc] = True
    for dr, dc in dist:
        nr = sr + dr
        nc = sc + dc

        if 0<=nr<N and 0<=nc<N and graph[nr][nc] == 1 and visited[nr][nc] == False:
            graph[nr][nc] = 0
            count += 1
            dfs(graph, nr, nc, visited)
            
    

grid = [list(map(int, input())) for _ in range(N)]
answer = []
for r in range(N):
    for c in range(N):
        if grid[r][c] == 1:
            count = 1
            tmp = dfs(grid, r, c, visit)
            answer.append(count)
answer.sort()
print(len(answer))
for i in answer:
    print(i)