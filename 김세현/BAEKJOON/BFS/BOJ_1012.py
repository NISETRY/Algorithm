from collections import deque

T = int(input())

def bfs(x, y, arr, N, M):
    q = deque()
    q.append([x, y])
    arr[y][x] = 0 # 방문

    while q:
        cx, cy = q.popleft() # 현재 칸 꺼내기

        for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
            nx = cx + dr
            ny = cy + dc

            # 범위 안이고, 아직 방문 안 했고, 배추 1 이라면
            if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 1:
                arr[ny][nx] = 0 # 방문 처리 (0으로 바꿔주기)
                q.append([nx, ny])


for _ in range(T):

    M, N, K = map(int, input().split()) # M 가로 N 세로 K 배추 위치 

    arr = [[0] * M for _ in range(N)] # 빈 배추밭

    for _ in range(K):
        x, y = map(int, input().split()) # 배추 좌표
        arr[y][x] = 1 # 현 배추 분포 입력하기

    cnt = 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1: # 배추 발견시
                bfs(x, y, arr, N, M)
                cnt += 1

    print(cnt)
