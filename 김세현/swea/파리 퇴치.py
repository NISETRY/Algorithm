T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0

            for x in range(i, i+M):
                for y in range(j, j+M):
                    s += arr[x][y]

            if max_v < s:
                max_v = s

    print(f'#{tc+1} {max_v}')


