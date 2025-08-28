from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_h = max(map(max, arr))

def bfs(x, y, h, visited):
    q = deque()
    q.append((x, y))
    visited[y][x] = True

    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx] and arr[ny][nx] > h:
                    visited[ny][nx] = True
                    q.append((nx, ny))

max_safe = 0
for h in range(0, max_h +1):

    visited = [[False]*N for _ in range(N)]

    cnt = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] > h and not visited[y][x]:
                bfs(x, y, h, visited)
                cnt += 1
    max_safe = max(max_safe, cnt)

print(max_safe)