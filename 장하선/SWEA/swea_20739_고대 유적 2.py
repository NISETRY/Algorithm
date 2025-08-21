T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    pic=[list(map(int,input().split())) for _ in range(n)]

    res=0
    for i in range(n):
        cnt=0
        for j in range(m):
            if pic[i][j]==1:
                cnt+=1
            else:
                res=max(res,cnt)
                cnt=0
        res=max(res,cnt)
    for j in range(m):
        cnt=0
        for i in range(n):
            if pic[i][j]==1:
                cnt+=1
            else:
                res=max(res,cnt)
                cnt=0
        res=max(res,cnt)
    if res==1:
        res=0
    print(f'#{tc} {res}')