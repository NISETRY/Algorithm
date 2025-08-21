T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_sum = 0
    
    for i in range(N):
        for j in range(N):
            # + 모양 합
            plus_sum = arr[i][j]
            for d in range(1, M):
                if i - d >= 0:
                    plus_sum += arr[i - d][j]
                if i + d < N:
                    plus_sum += arr[i + d][j]
                if j - d >= 0:
                    plus_sum += arr[i][j - d]
                if j + d < N:
                    plus_sum += arr[i][j + d]
            
            # x 모양 합
            x_sum = arr[i][j]
            for d in range(1, M):
                if i - d >= 0 and j - d >= 0:
                    x_sum += arr[i - d][j - d]
                if i - d >= 0 and j + d < N:
                    x_sum += arr[i - d][j + d]
                if i + d < N and j - d >= 0:
                    x_sum += arr[i + d][j - d]
                if i + d < N and j + d < N:
                    x_sum += arr[i + d][j + d]
            
            max_sum = max(max_sum, plus_sum, x_sum)
    
    print(f'#{tc} {max_sum}')