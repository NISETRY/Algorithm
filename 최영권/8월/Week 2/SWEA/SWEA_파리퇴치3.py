T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(N)]
    
    # + 경우
    max_t = 0
    for r in range(N):
        for c in range(N):

           
            # 일단 현재 위치 추가
            cur_sum = fly[r][c]
            for length in range(1, M):
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr = r + dx*length
                    nc = c + dy*length

                    if 0<=nr<=N-1 and 0<=nc<=N-1:
                        cur_sum += fly[nr][nc]
                    else:
                        continue
            if cur_sum > max_t:
                max_t = cur_sum                
    # X 경우
    max_x = 0
    for r in range(N):
        for c in range(N):
            
            # 일단 현재 위치 추가
            cur_sum = fly[r][c]
    
            for length in range(1, M):
                for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
                    nr = r + dx*length
                    nc = c + dy*length

                    if 0<=nr<=N-1 and 0<=nc<=N-1:
                        cur_sum += fly[nr][nc]
                    else:
                        continue
                    

            if cur_sum > max_x:
                max_x = cur_sum      
    print(f"#{tc} {max(max_t, max_x)}")