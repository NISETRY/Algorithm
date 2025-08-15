import pprint

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    monster = [list(map(int, input().split())) for _ in range(N)]
    dr = [1,-1,0,0]
    dc = [0,0, 1,-1]
    for r in range(N):
        for c in range(N):

            if monster[r][c] == 2:
                
                for dist in range(1, N):
                    for d in range(4):

                        nr = r + dr[d]*dist
                        nc = c + dc[d]*dist
                        
                        if 0<=nr<=N-1 and 0<=nc<=N-1 and monster[nr][nc] != 1:
                            monster[nr][nc] = 1                 

                        elif 0<=nr<=N-1 and 0<=nc<=N-1 and monster[nr][nc] == 1:
                            dr[d], dc[d] = 0, 0
    count = 0
    for i in range(N):
        for j in range(N):
            if monster[i][j] ==0:
                count += 1
    print(f"#{tc} {count}")