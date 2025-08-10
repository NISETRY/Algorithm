# # 스도쿠
# 1~9까지의 리스트 만들기
# 중복을 어떻게 해결하지
# 가로는 1:10
# 세로는 [1~10][i]
# 정사각형은 [1][123][2][123][3][123]
# from pprint import pprint as pprint
empty_9x9 = [[0] * 9 for _ in range(9)]


# empty_3x3x9 = [[0] * 3 for _ in range(3) for _ in range(9)]
# pprint.pprint(empty_3x3x9)

# 우선 만든 배열에 인풋을 넣자

# 조건문으로 행, 열, 칸이 모두 true 면 중복값 검정

# new_3x3x9 = [[[0]*3 for _ in range(3)] for _ in range(9)]
# pprint.pprint(new_3x3x9)
for test_case in range(int(input())):
    for i in range(9):
        empty_9x9[i] = list(map(int, input().split()))

    row = True
    for i in range(9):
        for j in range(1, 10):
            if empty_9x9[i].count(j) > 1:
                row = False
                break
            else:
                continue


    col = True
    for i in range(9):
        row_2_list = []
        for j in range(9):
            row_2_list.append(empty_9x9[j][i])
        for k in range(1,10):
            if row_2_list.count(k) > 1:
                col = False
                break
            else:
                continue


    box = True
    for i in range(3):
        box_2_list = []
        for j in range(3):
            box_2_list.append(empty_9x9[3 * i][j])
            box_2_list.append(empty_9x9[3 * i + 1][j])
            box_2_list.append(empty_9x9[3 * i + 2][j])
        for k in range(1, 10):
            if box_2_list.count(k) > 1:
                box = False
                break
            else:
                continue


    print(f'#{test_case + 1} {(row and col and box) * 1}')