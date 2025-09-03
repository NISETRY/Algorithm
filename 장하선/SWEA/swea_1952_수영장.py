# 정석 dp 버전
T=int(input())
for tc in range(1,T+1):
    price=list(map(int,input().split()))
    days=[0]+list(map(int,input().split()))
    dp=[0]+[3000*40]*12
    total=0
    for x in range(1,13):
        # 월간권과 일관권 비교 / 이전 달의 최소해에 이를 더함
        dp[x]=dp[x-1]+min(days[x]*price[0],price[1])
        # 3개월권을 비교 가능한 시점 : 3월부터
        if x>=3:
            dp[x]=min(dp[x],price[2]+dp[x-3])
        # 1, 2월은 3개월 전으로 못 가니까
        else:
            dp[x]=min(dp[x],price[2])
    # 최종 : 연간이랑 저 로직 중 싼 거 택하기
    total=min(price[3], dp[12])
    print(f'#{tc} {total}')