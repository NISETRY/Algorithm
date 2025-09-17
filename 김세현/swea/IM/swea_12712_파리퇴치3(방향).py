T = int(input())

for tc in range(T):

    N, M = map(int, input().split()) # NxN 크기, M 범위
    arr = [list(map(int, input().split()) for _ in range(N))]

    max_sum = 0
    dir_plus = [(-1,0), (1,0), (0,-1), (0,1)]
    dir_x = [(-1,-1), (-1,1), (1,-1), (1,1)]

    for i in range(N):
        for j in range(N):

        # + 모양
            plus_sum = arr[i][j] # 중심 

            for dx, dy in dir_plus:
                for d in range(1, M):
                    nx = i + dx * d
                    ny = j + dy * d
                    if 0 <= nx < N and 0 <= ny < N: # 범위 안에서만
                        plus_sum += arr[nx][ny]
                    else:
                        break

            # X 모양
            x_sum = arr[i][j] # 중심

            for dx, dy in dir_x:
                for d in range(1, M):
                    nx = i + dx * d
                    ny = j + dy * d
                    if 0 <= nx < N and 0 <= ny < N: # 범위 안에서만
                        x_sum += arr[nx][ny]
                    else:
                        break

            max_sum = max(max_sum, plus_sum, x_sum)

    print(f'#{tc} {max_sum}')

