T=int(input())
for tc in range(1,T+1):
    n,k=map(int,input().split())
    base=list(map(int,input().split()))
    max_team=[0]*n
    for zero_point in base:
        for i in range(n):
            if 0<=(zero_point-base[i])<=k:
            # if abs(zero_point-base[i])<=k:
                max_team[i]+=1
    max_val=max(max_team)
    print(f'#{tc} {max_val}')