T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    flies=[[0] for _ in range(n)]
    for x in range(n):
        lst=list(map(int,input().split()))
        flies[x]=lst
        max_val=0
    for i in range(n-m+1):
        for j in range(n-m+1):
            fly=0
            for x in range(m):
                for y in range(m):
                    fly+=flies[x+i][y+j]
            max_val=max(fly, max_val)
    print(f'#{tc} {max_val}')