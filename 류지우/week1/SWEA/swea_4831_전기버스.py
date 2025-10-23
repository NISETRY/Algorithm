# SWEA 4831번 전기버스

# 0번에서 출발해 종점인 N번 정류장까지 이동
# 한 번 충전으로 최대한 이동할 수 있는 정류장 수 k
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전으로 종점에 도착?
# 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0 출력
# 출발지에는 항상 충전기가 설치되었지만 충전횟수에는 포함 X


T = int(input()) # 노선 수

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stop = list(map(int, input().split())) # 충전소 위치

    # 버스 정류장 개수
    bus_stop = [0]*(N+1)

    charge = 0 # 충전횟수

    # 버스 정류장에 충전기가 있으면 1로 변경
    for i in range(len(bus_stop)):
        if i in charge_stop:
            bus_stop[i] = 1

    #  print(bus_stop)
    
    # 버스 위치
    bus_position = 0

    while (1):
        # 일단 버스 출발
        bus_position += K

        # 버스의 위치가 종점이거나 그 이상이면 종료
        if bus_position >= N:
            break
        
        # 일단 버스가 출발한거니까, 현재 위치에서 거꾸로 가면서 가까운 충전소 있으면 충전함.
        # 그럼 그 충전소가 현재 위치가 됨. 거기서 충전해야만 갈 수 있으니까
        for i in range(bus_position, bus_position-K, -1):
            if bus_stop[i] == 1:
                charge += 1
                bus_position = i
                break

        # 그 안에 충전소가 없으면, 충전을 못하니까 못도착함. 그래서 끝
        else:
            charge = 0
            break

    print(f'#{tc} {charge} ')



    # for i in range(len(bus_stop)):
    #     for j in range(len(bus_stop)-i):
    #         if 1 not in bus_stop[i:i+K]:
    #             charge = 0
    #             continue

    #         # bus_stop[i:i+K]에서 1이 제일 멀리 있는 인덱스로 내 위치 변경하고 charge += 1
    #         if bus_stop[i] == 1:

            
        



    # print(f'#{tc} {charge} ')