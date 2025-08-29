from collections import deque
import sys

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)] # 토마토 현 상태
q = deque()

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            q.append([i, j])

while q:
    i, j = q.popleft()

    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        x = i + di
        y = j + dj

        if 0 <= x < M and 0 <= y < N:
            if arr[x][y] == 0:
                # 며칠쨰인지 확인하기 위해
                arr[x][y] = arr[i][j] + 1
                q.append([x, y]) # 새로 1이 된 위치를 큐에 추가

ans = 0
for line in arr:
    for tomato in line:
        if tomato == 0:
            # 아직 익지 않은 토마토가 있으면 -1 출력 후 종료
            print(-1)
            sys.exit()
    ans = max(ans, max(line))

print(ans-1)


