# 사각형에 해당하는 만큼 1 입력
# 상하좌우로 0인 영역 찾아 나서기 

M, N, K = map(int, input().split())

arr = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            arr[y][x] = 1

from collections import deque

visited = [[0] * N for _ in range(M)] # 방문 여부 저장

def bfs(x, y):
    q = deque()
    q.append([x,y])
    visited[y][x] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if arr[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([nx, ny])
                    cnt += 1

    return cnt

v = []

for y in range(M):
    for x in range(N):
        if arr[y][x] == 0 and visited[y][x] == 0:
            cnt = bfs(x, y)
            v.append(cnt)

print(len(v))
v.sort()
print(*v)
