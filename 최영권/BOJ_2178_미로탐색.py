from collections import deque
N, M = map(int, input().split())
grid = []
for r in range(N):
    grid.append(list(input()))

def bfs(i, j, N, M):
    # 초기화
    count = 0
    visited = [[0]*M for _ in range(N)]# visited 생성
    q = deque()# 큐 생성, 시작점 인큐
    q.append((i, j))
    # 시작점 방문표시
    visited[i][j] = 1

    # 반복
    while q:           # 탐색할 정점이 남아있으면
        ti, tj = q.popleft()   # 디큐
        if (ti, tj) == (N-1, M-1):
            return visited[ti][tj]
    # visit(), 방문정점 출력
        for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
            wi, wj = ti + di, tj + dj
            if 0<=wi<N and 0<=wj<M and int(grid[wi][wj]) != 0 and visited[wi][wj] ==0:
                q.append((wi, wj))
                visited[wi][wj] = visited[ti][tj] + 1

    # 인접하고 미방문인 정점 인큐, 인큐표시
print(bfs(0,0,N,M))
