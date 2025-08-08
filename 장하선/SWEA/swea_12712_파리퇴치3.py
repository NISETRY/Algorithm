T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    flies=[[0] for _ in range(n)]
    for x in range(n):
        lst=list(map(int,input().split()))
        flies[x]=lst
        max_val=0
    

    print(f'#{tc} {max_val}')