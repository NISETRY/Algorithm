import sys
sys.stdin = open("input.txt")

# N // 2 개를 A 에 넣고, 나머지는 B 라고 가정
# -> 모든 재료를 골라보면서, A 에 넣자
# -> visited 로 구현 (1 이 라면  A 에 들어감, 0 이라면 B 에 들어감)


def cal_synergy(li):
    total = 0

    for i in range(len(li)):
        for j in range(i+1, len(li)):
            total += arr[li[i]][li[j]] + arr[li[j]][li[i]]


def get_synergy():
    A_list, B_list = [], []
    for i in range(N):
        if visited[i]:
            A_list.append(i)
        else:
            B_list.append(i)

        return cal_synergy(A_list), cal_synergy(B_list)

# 종료조건 : 재료의 반을 선택 --> 시너지 계산
# 가지의 수

def recur(cnt):
    if cnt == N // 2:
        # Todo: 시너지 계산
        return

    for food_number in range(N):
        if visited[food_number]:
            continue

        visited[food_number] = 1
        recur(cnt + 1)
        visited[food_number] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_answer = 21e8
    recur()
    print(f'#{tc} {min_answer}')