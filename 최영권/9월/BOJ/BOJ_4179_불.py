from collections import deque
import pprint
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
si, sj = N, M

def find(graph):
    global si, sj
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'J':
                si, sj = i, j
            if arr[i][j] == 'F':
                fire.append((i, j))
    
fire = deque()

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
def bfs(r, c, bull):
    if r == 0 or r == N-1 or c == 0 or c == M-1:
            return 1
    q = deque()
    q.append((r, c))
    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 0

    while q:
        for _ in range(len(bull)):
            fr, fc = bull.popleft()  
            for d in range(4):
                nfr, nfc = fr+dr[d], fc+dc[d]
                if nfr<0 or nfr>=N or nfc<0 or nfc>=M:
                    continue
                if arr[nfr][nfc] != '#' and arr[nfr][nfc] != 'F':
                    arr[nfr][nfc] = 'F'
                bull.append((nfr, nfc))
        
        
        for _ in range(len(q)):
            sr, sc = q.popleft()
            for d in range(4):
                nr, nc = sr+dr[d], sc+dc[d]
                if nr<0 or nr>=N or nc<0 or nc>=M:
                    continue
                if arr[nr][nc] == 'F' or arr[nr][nc] == '#' or visited[nr][nc]:
                    continue
            
                if nr == 0 or nr == N-1 or nc == 0 or nc == M-1:
                    visited[nr][nc] = visited[sr][sc] + 1
                    return visited[nr][nc] + 1
                q.append((nr, nc))
                visited[nr][nc] = visited[sr][sc] + 1
            
    return "IMPOSSIBLE"
    
find(arr)
print(bfs(si, sj, fire))
