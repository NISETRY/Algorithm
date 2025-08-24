import pprint
from collections import deque
T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M, K = map(int,input().split())

    laddish = [[0] * M for _ in range(N)]
    for _ in range(K):
        row, col = map(int, input().split())
        laddish[row][col] = 1
    pprint.pprint(laddish)
    count = 0
    # q = deque()
    # for r in range(N):
    #     for c in range(M):
    #         q.append((r,c))
            
    #         while q:
                
    #             lr, lc = q.popleft()
    #             if laddish[lr][lc] == 1:
                    
    #                 laddish[lr][lc] = 0
    #                 for d in range(4):
    #                     nr = lr + dr[d]    
    #                     nc = lc + dc[d]
    #                     if 0<=nr<N and 0<=nc<M and laddish[nr][nc] == 1:
    #                         q.append((nr, nc))
    #         count += 1
    for i in range(N):
        for j in range(M):
            # 만약 배추가 있고 아직 방문하지 않았다면
            if laddish[i][j] == 1:
                # 새로운 그룹을 찾았으므로 count +1
                count += 1

                # 찾은 r,c로부터 너비우선탐색(BFS)
                q = deque([(i, j)])
                # 시작점 방문처리
                laddish[i][j] = 0
                # BFS로 현재 r,c에서 지렁이가 갈 수 있는 양배추 모두 0으로 바꿔주기
                while q:
                    # 큐에서 가야할 곳 선정
                    cur_y, cur_x = q.popleft()

                    # 4방향 탐색
                    for d in range(4):
                        nc = cur_y + dr[d]
                        nr = cur_x + dc[d]
                        if 0<=nc<N and 0<=nr<M and laddish[nc][nr] == 1:
                            laddish[nc][nr] = 0
                            q.append((nc,nr))

    print(count)