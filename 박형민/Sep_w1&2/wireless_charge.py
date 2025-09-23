from pprint import pprint as print

T = int(input())

dr = [0, 0, 1, 0, -1]
dc = [0, -1, 0, 1, 0]

for tc in range(1, T+1):
    N, BC_count = map(int, input().split())
    A_path = list(map(int, input().split()))
    B_path = list(map(int, input().split()))
    A_path.insert(0, 0)
    B_path.insert(0, 0)

    A = [1, 1]
    B = [10, 10]
    answer = 0

    BC_info = [0]*BC_count
    for i in range(BC_count):
        BC_info[i] = tuple(map(int, input().split()))

    # 순차적으로 이동하며 충전하기
    for step in range(N+1):
        # 1. A와 B를 이동하기
        a_dir, b_dir = A_path[step], B_path[step]
        A[0] += dr[a_dir]
        A[1] += dc[a_dir]
        B[0] += dr[b_dir]
        B[1] += dc[b_dir]

        A_BCs = []
        B_BCs = []

        for i in range(len(BC_info)):
            BC_r, BC_c, distance, charge = BC_info[i]

            if abs(A[0] - BC_r) + abs(A[1] - BC_c) <= distance:
                A_BCs.append((i, charge))
            if abs(A[0] - BC_r) + abs(A[1] - BC_c) <= distance:
                B_BCs.append((i, charge))

            A_BCs.sort(key=lambda x: x[1], reverse=True)
            B_BCs.sort(key=lambda x: x[1], reverse=True)

        # 2. A, B 각각이 충전 가능한 충전소를 파악하기

        # 3. 최대 충전량이 확보 가능한 충전기를 고르기
        #       i. 충전기가 겹치지 않는 경우
        set_BCs = set(A_BCs).union
        if len(set_BCs) == len(A_BCs) + len(B_BCs):
        #       ii. 충전기가 겹치는 경우
        #

# M, BC_count = 20, 3    # M: total moved time / A: numbers of BC(Battery Charge Point)
# arr = [ [0] * 10 for _ in range(10) ]
#
# powers = [0]
#
# for k in range(1, BC_count+1):
#     cp_x, cp_y, d, pw = map(int, input().split())    # cp: charge_point, pw: power
#     cp_r, cp_c = cp_y - 1, cp_x - 1
#
#     powers.append(pw)
#
#     for i in range(10):
#         for j in range(10):
#             if abs(cp_r - i) + abs(cp_c - j) <= d:
#                 if arr[i][j] == 0:         # 조건문 설명:
#                     arr[i][j] = [0]         # 충전소 번호가 1 부터 시작하므로 idx 상 번호 유지를 위해
#                     arr[i][j].append(pw)     # 충전 범위인 곳은 list 로 바꿔서 충전소 번호를 해당 idx 에 넣고,
#                 else:
#                     arr[i][j].append(pw)     # 이미 범위인 곳은 새로운 충전소 번호도 append 하여 해당 idx 의 정보를 list 로 저장
#
# print(arr)
# # 충전소 정보가 있는 arr 과 각 충전소의 출력을 나타낸 powers
#
# # 제상우하좌(rc가 행열이 바뀌어 있음)
