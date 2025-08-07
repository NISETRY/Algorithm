for tc in range(10):
    input()
    matrix=[list(map(int, input().split())) for _ in range(100)]
    # for i in range(100):
    #     arr = list(map(int, input().split()))
    #     matrix[i]=arr
    # matrix = [arr[i:i+100] for i in range(0, 10000, 100)]


    # 행의 합 최대 구하기
    s = []
    for i in range(len(matrix)):    
        s.append(sum(matrix[i]))
    r = max(s)

    # 열의 합 최대 구하기
    col_sum = [sum(row[i] for row in matrix) for i in range(100)] # for row in matrix 행들을 하나씩 row에 담아서 반복
    c = max(col_sum)


    # 대각선의 합 최대 구하기
    sum_a = []
    sum_b = []
    for i in range(100):
        sum_a.append(matrix[i][i])
        sum_b.append(matrix[i][99-i])
    d1 = sum(sum_a)
    d2 = sum(sum_b)

    print(f'#{tc+1} {max(r, c, d1, d2)}')
