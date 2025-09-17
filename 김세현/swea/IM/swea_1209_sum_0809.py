for tc in range(10):

    input()

    arr = [list(map(int, input().split())) for _ in range(100)]

    # 가로
    max_row = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        
        if max_row < sum:
            max_row = sum

    # 세로
    max_col = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[j][i]
        
        if max_col < sum:
            max_col = sum

    # 대각선
    sum1 = 0
    sum2 = 0
    for i in range(100):
        sum1 += arr[i][i]
        sum2 += arr[i][99-i]

    result = max(max_row, max_col, sum1, sum2)

    print(f'#{tc+1} {result}')


