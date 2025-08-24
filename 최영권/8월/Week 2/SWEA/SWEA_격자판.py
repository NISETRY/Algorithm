# NxN의 격자판이있다
# 격자의 각 칸에는 정수가 하나씩 적혀있다
# 공은 어떤 칸에서 시작해서 상하좌우로 이동할 수 있다
# 단, 이동할 수 있는 조건은 현재 칸보다 숫자가 작은 칸으로만 이동 가능하다
# 이동할 때마다 공은 한 칸 씩 이동하며 이동할 수 있을 때까지 계속 이동한다
# 가장 많이 이동할 수 있는 경우의 이동 횟수를 구하는 문제다
# 정확히는 출발칸을 포함한 이동한 칸의 수를 세는 것
# 정리하면
# 어디서 출발하면 가장 많이 이동할 수 잇을 지 찾고 그 최대 이동 수를 구하는 문제
# 시작할 때 i,j 칸에서 출발해서
# 매번 인접한 칸 상하좌우 중 자기보다 작은 값이 있으면 그쪽으로 이동
# 이동을 반복하다가 더 이상 갈 곳이 없으면 이동을 멈춘다
# 출발할 수 있는 모든 칸을 다 시도해서, 그 중 가장 많은 이동수를 찾는 문제
# 이동할 때 마다 이동 칸 수 plus를 세기
# 모든 칸에 대해 시작해서 최대 이동 길이를 구한다

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0
    for i in range(N):
        for j in range(N):
            data = []
            count = 0
            while True:
                if arr[i][j] < arr[i][j+1] and arr[i][j] < arr[i][j-1] and arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i+1][j]:
                    break
                if 0 <= i+1 < N:
                    data.append(arr[i+1][j])
                else:
                    data.append(float('inf'))
                if 0 <= i-1 < N:
                    data.appned(arr[i-1][j])
                else:
                    data.append(float('inf'))
                if 0 <= j+1 < N:
                    data.append(arr[i][j+1])
                else:
                    data.append(float('inf'))
                if 0 <= j-1 < N:
                    data.append(arr[i][j-1])
                else:
                    data.append(float('inf'))
                min_data = data[0]
                min_idx = 0
                for r in range(len(data)):
                    if data[r] < min_data:
                        min_data = data[r]
                        min_idx = r
                    if r == 0:
                        i += 1
                    elif r == 1:
                        i -= 1
                    elif r == 1:
                        j += 1
                    elif r == 1:
                        j -= 1
                count += 1
            if max_count < count:
                max_count = count
    print(f'#{tc} {max_count}')
                