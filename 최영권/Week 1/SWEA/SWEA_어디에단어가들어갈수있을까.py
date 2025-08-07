T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    # 가로
    for r in range(N):
        r_sum = 0
        for c in range(N):
            # 가로 합
            if puzzle[r][c] == 1:
                r_sum += 1
            if puzzle[r][c] == 0 or c == N-1:
                if r_sum == K:
                    count+=1
                r_sum = 0
        
    for r in range(N):
        c_sum = 0
        for c in range(N):        
            if puzzle[c][r] == 1:
                c_sum += 1
            if puzzle[c][r] == 0 or c == N-1:
                if c_sum == K:
                    count += 1
                c_sum = 0
    print(f"#{tc} {count}")

            # 세로합
            # 전체합
