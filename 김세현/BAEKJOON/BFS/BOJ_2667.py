from collections import deque

N = int(input())

house = []

for _ in range(N):
    row = list(map(int, input())) 
    house.append(row)

visited = [[0] * N for _ in range(N)]
v = []

def dfs(x, y):
    q = deque()
    q.append([x, y])
    visited[y][x] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if house[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([nx, ny])
                    cnt += 1

    return cnt

for y in range(N):
    for x in range(N):
        if house[y][x] == 1 and visited[y][x] == 0:
            cnt = dfs(x, y)
            v.append(cnt)

v.sort()
print(len(v))
for val in v:
    print(val)


    
