T = int(input())

for tc in range(T):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    # 가로줄, 세로줄 저장해놓기

    sum_garo = [0] * N
    sum_sero = [0] * N

    for i in range(N):
        for j in range(N): 
            sum_garo[i] += arr[i][j]
            sum_sero[i] += arr[j][i]
        

    for i in range(N):
        sum_i = 0
        for j in range(N):
            sum_i = sum_garo[i] + sum_sero[j] - arr[i][j]

            if sum_i > max_sum:
                max_sum = sum_i
            print(sum_i)

    print(f'#{tc+1} {max_sum}')

