t = int(input())
for tc in range(t):
    n, m = map(int, input().split()) # 사이즈, 지불가능비용
    graph = [list(map(int, input().split())) for _ in range(n)] 
    house = [(p,q) for p in range(n) for q in range(n) if graph[p][q] == 1] # 집만 모음
    max_house = 0

    for i in range(n):
        for j in range(n):
                                  # 최대 n은 20
            dist = [0]*40         # 거리의 최대 = (0,0)-(19,19) = 40                 
            for hi, hj in house: 
                t = abs(i-hi) + abs(j-hj) + 1  # 스타트 지점과 집과의 거리 구함
                dist[t] += 1      # 거리 + 1

            cnt = 0
            for k in range(1,40): 
                cnt+=dist[k]      # 거리별 누적 개수 세고
                if cnt*m >= k*k + (k-1)*(k-1) and cnt>max_house: # 그게 코스트보다 크면 갱신 
                    max_house = cnt

    print(f'#{tc+1} {max_house}')