T = int(input())

for tc in range(T):

    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    count_c = 0
    result_c = 0

# 가로 방향 검사
    for i in range(N):
        count_c = 0
        for j in range(N): #열을 순회하며 1을 세기
            if arr[i][j] == 1:
                count_c += 1

            if arr[i][j] == 0 or j == N-1:
                if count_c == K:
                    result_c += 1

                count_c = 0 # 연속이 끊겼으므로 카운트 초기화
  


    count_r = 0
    result_r = 0

# 세로 방향 검사
    for j in range(N):
        count_r = 0
        for i in range(N): # 행을 순회하며 1을 세기
            if arr[i][j] == 1:
                count_r += 1

            if arr[i][j] == 0 or i == N-1:
                if count_r == K:
                    result_r += 1

                count_r = 0

    print(f'#{tc+1} {result_c + result_r}')
                
                    
                