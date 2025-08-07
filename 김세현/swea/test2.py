# 파리 퇴치 복습

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_kill = 0

for i in range(N-M+1):
    for j in range(N-M+1):
        num = 0
        for x in range(i, i+M):
            for y in range(j, j+M):
                num += arr[x][y]

        if num > max_kill:
            max_kill = num

print(max_kill)