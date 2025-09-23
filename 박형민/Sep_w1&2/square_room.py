# 현재 위치 숫자 기준 상하좌우를 확인
# -> 1 큰게 있으면 visited 에 1 이라고 체크
import sys
sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)

    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                if arr[ny][nx] == arr[y][x] + 1:
                    # 현재 숫자는 다음으로 이동 가능함을 표시
                    visited[arr[y][x]] = 1
                    break   # 다른 방향은 볼 필요없음

                max_cnt = 0     # 정답
                cnt = 0         # 하나하나 마다 몇 개가 연속되는지?
                start = 0       # 숫자를 세기 시작한 위치

                for i in range(1, N * N + 1):
                    if visited[i] == 1:
                        cnt += 1
                    else:
                        if max_cnt < cnt:
                            max_cnt = cnt
                            start = i - cnt
                        cnt = 0

    print(f'#{tc} {start} {max_cnt}')
