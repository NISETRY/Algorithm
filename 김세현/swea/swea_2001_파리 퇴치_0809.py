T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0 

    # 시작점 배정
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0 # 값 저장해 둘 공간
            for x in range(M):
                for y in range(M):
                    sum += arr[x+i][y+j]

            if max_sum < sum:
                max_sum = sum
            
    print(f'#{tc+1} {max_sum}')