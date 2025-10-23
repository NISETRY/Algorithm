# 윤태양 코드

t = int(input())
for i in range(t):
    k, n, m = map(int, input().split())
    m_list = list(map(int, input().split()))

    last = 0                    # 변수명 변경
    stop = 0
    energy = k
    now = 0
    for_break = False

    while now != n:            # 에너지가 없을 때까지 이동
        now+=1
        energy-=1

        if energy == 0:        # 에너지가 0인데, 종점이다? break
            if now == n:
                break

            while now not in m_list:    # 에너지가 0인데, 종점 아니다 -> 충전소가 나올 때까지 한칸씩 후진
                now-=1

            if last == now:             # 도달한 충전소가 마지막 충전한 충전소와 같으면 break -> 종점 가는 게 불가
                for_break = True
                break

            energy=k                    # 충전시 energy 리셋
            stop+=1                     # 충전횟수 +=1
            last = now                  # 충전소 업데이트

    if for_break == True:              # 종점 못가는 경우
        print(f'#{i+1} 0')
    else:                              # 종점 가는 경우
        print(f'#{i+1} {stop}')



# 최영권
