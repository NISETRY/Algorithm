import pprint
from collections import deque
N, M = map(int, input().split())
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]  # 3차원 


def bfs():
    q = deque()
    visited[0][0][0] = 1
    q.append((0,0,0))  # k는 벽을 뿌신 횟수, r, c

    step = 1
    while q:

        for _ in range(len(q)):
            
            k, r, c = q.popleft()

            if r == N-1 and c == M - 1:
                return step
            for dir in range(4):
                nk = k
                nr = r + dr[dir]
                nc = c + dc[dir]
                
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue 
                # else를 쓸 수 없음
                if graph[nr][nc] == 1:
                    if nk == 1 or visited[1][nr][nc]:
                        continue
                    nk = 1

                else:
                    if visited[nk][nr][nc]:
                        continue
                visited[nk][nr][nc] = 1
                q.append((nk, nr, nc))
        step += 1
    return -1
#         sr, sc = q.popleft()
#         for d in range(4):
#             nr = sr + dr[d]
#             nc = sc + dc[d]
#             if 0<=nr<N and 0<=nc<M and graph[nr][nc] == 0 and visited[nr][nc] == 0:
#                 visited[nr][nc] = 1
#                 count += 1
#                 q.append([nr, nc])
#             elif 0<=nr<N and 0<=nc<M and graph[nr][nc] == 1:
#                 nr += dr[d]
#                 nc += dc[d]
#                 if 0<=nr<N and 0<=nc<M and graph[nr][nc] == 0 and visited[nr][nc] == 0:
#                     visited[nr][nc] = 1
#                     count += 1
#                     q.append([nr, nc])
print(bfs())



# print(count)