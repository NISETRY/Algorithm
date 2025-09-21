from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs():
    q = deque()
    q.append((K, 0, 0))  # r, c, k
    best = [[-1]*M for _ in range(N)]
    best[0][0] = K
    total = 1

    while q:
        for _ in range(len(q)):
            k, r, c  = q.popleft()
            if r == N-1 and c == M-1:
                return total
            
            for dir in range(4):
                nk, nr, nc = k, r+dr[dir], c+dc[dir]                
                if nr<0 or nr>=N or nc<0 or nc>=M:
                    continue

                if arr[nr][nc] == 1:
                    if nk == 0:
                        continue
                    nk -= 1

                if nk <= best[nr][nc]:
                    continue
                best[nr][nc] = nk
                if nr == N-1 and nc == M-1:
                    return total + 1
                q.append((nk, nr, nc))
        total += 1
    return -1

print(bfs())
