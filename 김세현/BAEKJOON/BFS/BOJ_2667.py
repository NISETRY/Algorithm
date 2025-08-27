from collections import deque

N = int(input())

house = []

for _ in range(N):
    row = list(map(int, input())) 
    house.append(row)

visited = [[0] * N for _ in range(N)] # 방문 여부 저장
v = [] # 단지별 집 수 저장

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[y][x] = 1
    cnt = 1 # 시작점도 1이므로 1부터 시작

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

# 전체 지도 순회/ DFS 시작점 찾기
# 집이고 방문하지 않은 곳이면
for y in range(N):
    for x in range(N):
        if house[y][x] == 1 and visited[y][x] == 0:
            cnt = bfs(x, y)
            v.append(cnt)

v.sort() # 오름차순 정렬
print(len(v))
for val in v:
    print(val)