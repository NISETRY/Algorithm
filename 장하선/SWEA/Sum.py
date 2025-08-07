for tc in range(1,11):
    row=0
    col_sum = [0]*100
    cro_sum_1 = cro_sum_2 = 0
    # 입력
    input()
    for i in range(100):
        num_list=list(map(int, input().split()))
        s=sum(num_list)
        if s>row:
            row=sum(num_list)
        for idx, num in enumerate(num_list):
            col_sum[idx]+=num
        cro_sum_1+=num_list[i]
        cro_sum_2+=num_list[99-i]
    col=max(col_sum)
    res=max(row, col, cro_sum_1, cro_sum_2)
    print(f'#{tc} {res}')