T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count_a = 0
    max_count_b = 0

    # 가로 최대 값
    for i in range(N):
        count_a = 0
        for j in range(M):
            if arr[i][j] == 1: # 1인 경우 count += 1
                count_a += 1
                if j == M-1: # 1이 가장 마지막 값이 경우, 바로 개수를 확인
                    if count_a > max_count_a:
                        max_count_a = count_a
            else: # 0인 경우 지금까지의 count를 바로 확인하여 최대 값인지 확인
                if count_a > max_count_a:
                    max_count_a = count_a
                count_a = 0


    # 세로 최대 값
    for i in range(M):
        count_b = 0
        for j in range(N):
            if arr[j][i] == 1:
                count_b += 1
                if j == N-1:
                    if count_b > max_count_b:
                        max_count_b = count_b
            else:
                if count_b > max_count_b:
                    max_count_b = count_b
                count_b = 0

    max_count = max(max_count_a, max_count_b)

    if max_count == 1:
        max_count = 0
    
    print(f'#{tc+1} {max_count}')