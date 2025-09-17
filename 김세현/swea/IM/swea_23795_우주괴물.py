N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 값이 2이면 우주괴물 위치
# 상하좌우로 0이면 광선 1 이면 벽이라 막힘

cnt = 0

dirs = [[-1,0], [0,-1], [1,0], [0,1]]

for x in range(N):
    for y in range(N):
        if arr[x][y] == 2:
            for dx, dy in dir:
                for k in range(1, N):
                    nx = x + dx * k
                    ny = y + dy * k

                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        break
                    else:
                        if arr[nx][ny] == 1:
                            break
                        if arr[nx][ny] == 0:
                            cnt += 1
 
print(cnt)