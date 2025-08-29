# 백준 2206번 벽 부수고 이동하기
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = [list(map(int,input())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(2)] # 3차원

def bfs():

    q = deque()
    visited[0][0][0] = 1
    q.append((0, 0, 0)) # k(벽을 부순 횟수), r, c

    # 도착지까지의 발걸음 수를 셀 것
    step = 1 # 출발한 곳, 도착한 곳 포함해서 step을 셀 것

    while q:

        for _ in range(len(q)):
            k, r, c = q.popleft()

            if r == N-1 and c == M-1:
                return step

            for dir in range(4):
                nk = k
                nr = r + dr[dir]
                nc = c + dr[dir]

                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue

                if graph[nr][nc] == 1:
                    if nk == 1  or visited[1][nr][nc]:
                        continue
                    nk = 1
                    # visited[nk][nr][nc] = 1
                    # q.append((nk,nr,nc))
                else:
                    if visited[nk][nr][nc]:
                        continue
                    # visited[nk][nr][nc] = 1
                    # q.append((nk,nr,nc))

                # 공통으로 작성된거니까    
                visited[nk][nr][nc] = 1
                q.append((nk,nr,nc))

        step += 1
        
    return -1

print(bfs()) # 시작점을 알려줄 필요가 없음. 0,0이기도 하고, 일회성 호출임(재귀가 아님)