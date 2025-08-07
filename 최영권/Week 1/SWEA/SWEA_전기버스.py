# 충전만큼만 갈 수 있어
# 한 번 충전했을때 K개 만큼만 갈 수 있어
# Testcase로 로직 확인

## 풀이 1
# T = int(input())
# for tc in range(1, T+1):
#     k, n, m = map(int, input().split())

    # init_k = k
    # stop = list(map(int, input().split()))
    # charge = 0
#     for i in range(1, n+1):
        
#         # 연료 소진
#         k-=1

#         # 도달 불가능한 경우
#         if k < 0:
#             charge = 0
#             break

#         # 충전소가 없는 정류장일 경우
#         if i not in stop:
#             continue

#         # 종점과 다음 충전소에 못갈때 충전하기
#         # 1. 남은 연료로 종점에 가지 못하면 (기본조건)
#         # 2. 다음 충전소도 못갈만큼 연료가 남았으면
#         # 2-1 여기가 마지막 충전소인 경우
#         # 2-2 내가 다음 충전소까지 연료가 부족한 경우
#         if i+k < n and (stop.index(i) == len(stop)-1 or i+k < stop[stop.index(i)+1]):
#             k = init_k
#             charge += 1

#     print(f"#{tc} {charge}")


## 풀이 2
# 헤딩 지점에 갔을 때 충전 할지 말지가 중요
# 굳이 한 칸씩 움직여야되나?

# 종점에 도달할 수 있을 때 까지
    # charges = list(map(int, input().split()))
    # position = 0
    # fuel = k
    # recent_stop_idx = 0
    # answer = 0
    # # 다음 지점으로 갈 수 있는 곳을 탐색
    #     # 충전소 번호만 보고 탐색
    #     # 1,3,5,7,9

    # # 
    # while position + fuel < n:
    #     # 다음 충전소 탐색
    #     # 그 전에 백업
    #     next_stop_idx = recent_stop_idx

    #     for idx in range(recent_stop_idx+1, m):
    #         if charges[idx] > position+fuel:
    #             break
    #         next_stop_idx = idx
    #     if next_stop_idx == recent_stop_idx:
    #         answer = 0
    #         break

    #     position = charges[next_stop_idx]
    #     answer += 1
    #     recent_stop_idx = next_stop_idx
    # print(f"#{tc} {answer}")

    
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
    # stations.append(N)           # 도착지를 충전소 목록에 추가

    position = 0                 # 현재 위치
    charge_count = 0             # 충전 횟수

    # 도착지에 다다를 수 있을 때까지 반복
    while position + K < N:
        # 갈 수 있는 범위(position, position+K] 내 충전소만 골라서
        reachable = [s for s in stations if position < s <= position + K]
        if not reachable:
            # 한 칸도 못 가면 종료하고 0 리턴
            charge_count = 0
            break
        # 가장 먼 곳으로 이동(충전)
        position = reachable[-1]
        charge_count += 1

    print(f"#{tc} {charge_count}")