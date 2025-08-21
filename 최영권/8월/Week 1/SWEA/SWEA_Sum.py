T = 10

for tc in range(1, T+1):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_lst = []
    for i in range(100):
        row_s = 0
        for j in range(100):
            row_s += arr[i][j]
        sum_lst.append(row_s)

    for i in range(100):
        col_s = 0
        for j in range(100):
            col_s += arr[j][i]
        sum_lst.append(col_s)
    right_sum = 0
    left_sum = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                right_sum += arr[i][j]
        
            if i == 99 - j:
                left_sum += arr[i][j]
    sum_lst.append(right_sum)
    sum_lst.append(left_sum)

    print(f"#{tc} {max(sum_lst)}")