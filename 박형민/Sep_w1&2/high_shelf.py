# 2 ** 20 만큼의 연산
# 부분집합 문제
# 부분집합 : 수가 정해져 있지 않음
#   -> 모든 원소에 대해 포함할지 말지를 결정. (순서와는 무관. 포함/미포함만 따짐)
# 조합 : 수가 정해져 있음
#   -> 특정 개수만큼 원소를 고정된 수만큼 고르는 경우

# 이 문제는 몇 개를 고를지 정해져 있지 않기 때문에 부분집합

import sys
sys.stdin = open("input.txt.")

# 종료조건: N명의 모든 점원을 고려했을 때
#   - 가지치기: 이미 높이가 B 이상이면 더 이상 쌓을 필요 없다
# 가지의 수:
#   - 점원을 탑에 포함 시키는 경우 or 안 시키는 경우


def recur(idx, total_height):
    if idx == N:    # N명을 모두 고려함
        return

    recur(idx + 1, total_height + heights[idx])  # 탑에 포함 시키는 경우
    recur(idx + 1, total_height)  # 탑에 포함 안 시키는 경우
    pass


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_answer = 1e8            # 나올 수 있는 최대 범위 (정답이 항상 보장된 경우)
    # min_answer = 10000 *      # 나올 수 없다면 최대 값으로
    recur(0, 0)
    print(f'#{tc}')
