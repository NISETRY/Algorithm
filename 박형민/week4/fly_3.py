T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0


    plus_di = [1, 0, -1, 0]
    plus_dj = [0, 1, 0, -1]

    cross_di = [1, 1, -1, -1]
    cross_dj = [1, -1, -1, 1]


    for i in range(N):
        for j in range(N):
            plus_flies = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + plus_di[k] * l
                    nj = j + plus_dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        plus_flies += arr[ni][nj]
            
            cross_flies = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + cross_di[k] * l
                    nj = j + cross_dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        cross_flies += arr[ni][nj]
            
            result = max(result, cross_flies, plus_flies)

    print(f'#{tc} {result}')