T=int(input())
for tc in range(1,T+1):
    n=int(input())
    ballons=[list(map(int,input().split())) for _ in range(n)]
    max_val=0
    rev_ballons=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rev_ballons[i][j]=ballons[j][i]
    row_sum=[]
    col_sum=[]
    for i in range(n):
        row_sum.append(sum(ballons[i]))
    for i in range(n):
        col_sum.append(sum(rev_ballons[i]))
    for i in range(n):
        for j in range(n):
            max_val=max(row_sum[i]+col_sum[j]-ballons[i][j],max_val)
    print(f'#{tc} {max_val}')