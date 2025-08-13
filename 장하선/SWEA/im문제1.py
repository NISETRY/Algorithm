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

T=int(input())
for tc in range(1,T+1):
    n,k=map(int,input().split())
    stats=list(map(int,input().split()))
    ans=1 # 1명이면 팀 짜는거 고려 안하니까 initialvalue는 1로
    stats.sort()
    # 2인 팀 구성 가능여부 확인
    for i in range(n-1): # 첫 번째 기준점
        temp=1 # 팀원 수가 몇 명 누적되었는지 확인할 임시 변수
        for j in range(i+1, n): # 두 번째 기준점
            if stats[j]-stats[i]>k:
                break
            temp+=1
        ans=max(ans,temp)
    print(f'#{tc} {ans}')

T=int(input())
for tc in range(1,T+1):
    n,k=map(int,input().split())
    stats=list(map(int,input().split()))
    ans=1 # 1명이면 팀 짜는거 고려 안하니까 initialvalue는 1로
    stats.sort()
    left, right=0, 0
    while right<n:
        if stats[right]-stats[left]<=k:
            right+=1
            continue
        ans=max(ans, right-left+1)
        left+=1
    print(f'#{tc} {ans}')