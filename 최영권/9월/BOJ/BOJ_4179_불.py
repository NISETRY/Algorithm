from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

fire = deque()
jihun = deque()
visited = [[0]*M for _ in range(N)]  # 지훈 방문만 기록

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'F':
            fire.append((i, j))
        elif grid[i][j] == 'J':
            jihun.append((i, j))
            visited[i][j] = 1

def bfs():
    time = 0
    while jihun:
        time += 1

        # 1) 불 먼저 확산
        for _ in range(len(fire)):
            r, c = fire.popleft()
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == '.':
                    grid[nr][nc] = 'F'
                    fire.append((nr, nc))

        # 2) 지훈 이동
        for _ in range(len(jihun)):
            r, c = jihun.popleft()
            # 가장자리에 있으면 탈출 성공
            if r == 0 or r == N-1 or c == 0 or c == M-1:
                return time
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    if not visited[nr][nc] and grid[nr][nc] == '.':
                        visited[nr][nc] = 1
                        jihun.append((nr, nc))
    return "IMPOSSIBLE"

print(bfs())
