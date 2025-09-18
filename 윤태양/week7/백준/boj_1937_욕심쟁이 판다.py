import sys
sys.setrecursionlimit(10**7)

def dfs(a, b):
    # 이미 계산된 값이 있으면 바로 반환
    if visited[a][b] != 0:
        return visited[a][b]
    
    visited[a][b] = 1  # 자기 자신만 포함해도 길이 1
    for dx, dy in move:
        nx, ny = a + dx, b + dy
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[a][b]:
            visited[a][b] = max(visited[a][b], 1 + dfs(nx, ny))
    
    return visited[a][b]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [[-1,0],[1,0],[0,1],[0,-1]]
visited = [[0]*n for _ in range(n)]

answer = -1
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)
