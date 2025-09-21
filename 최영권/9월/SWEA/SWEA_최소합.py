T = int(input())

def dfs(r, c, visited):
    global total
    global answer
    visited[r][c] = 1
    if r!=N-1 and c!=N-1 and arr[r][c] == max(map(max, arr)):
        return
    if r == N-1 and c == N-1:
        answer = min(answer, total)
        return
    for dr, dc in [(0,1), (1,0)]:
        nr,nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0:
            total += arr[nr][nc]
            visited[nr][nc] = 1
            dfs(nr, nc, visited) 
            total -= arr[nr][nc]
            visited[nr][nc] = 0
            
INF = float('inf')
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    answer = INF
    total = arr[0][0]
    dfs(0,0, visited)
    print(f"#{tc} {answer}")