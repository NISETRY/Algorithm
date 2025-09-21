from collections import deque
N, M = map(int, input().split())

dr = [1, -1, 0, 0]
dc = [0, 0, -1 , 1]
def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    step = 1
    while q:
        for i in range(len(q)):
            k, r, c = q.popleft()
            if r == N - 1 and c == M - 1:
                return step

            for dir in range(4):
                nr, nc = r+dr[dir], c+dc[dir]
                nk = k
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                
                if arr[nr][nc]:
                    if nk == 1 or visited[1][nr][nc]:
                        continue
                    nk = 1
                else:
                    if visited[nk][nr][nc]:
                        continue
                q.append((nk, nr, nc))
                visited[nk][nr][nc] = 1
        step += 1
    return -1


arr = [list(map(int,input())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]

print(bfs())
