T=int(input())
for tc in range(1,T+1):
    k,n,m=map(int, input().split())
    init_k=k
    charge=0
    # 충전소 input
    spot=list(map(int, input().split()))
    # 정류장 별 연료 현황 기록
    fuel=[0]*(n+1)
    for i in range(n+1):
        if i in spot:
            cur_spot=spot.index(i)
            # 마지막 충전소가 아닌 모든 충전소에서
            if cur_spot<m-1:
                # 현재 idx+남은 연료 k로 다음 충전소에 갈 수 없다면 연료 보충
                if i+k<spot[cur_spot+1]:
                    k=init_k
                    charge+=1
            # 마지막 충전소에서
            else:
                if i+k<n:
                    k=init_k
                    charge+=1
        # 현재 연료량 기록
        fuel[i]=k
        # 다음 지점으로 가기에, 연료 소모
        k-=1
    # 연료가 0이 되어 마지막 지점에 가더라도 상관 없으니 연산에 방해되는 마지막 요소 제거
    fuel.pop()
    # 그럼에도 불구하고 연료 항목에 0이 있었으면 charge를 0으로
    if 0 in fuel:
        charge=0
    print(f'#{tc} {charge}')