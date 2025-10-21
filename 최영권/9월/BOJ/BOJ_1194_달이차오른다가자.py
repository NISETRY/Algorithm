import sys 
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

info = {
    'road':'.',
    'wall':'#',
    'key' : ('a', 'b', 'c', 'd', 'e', 'f'),
    'door': ('A', 'B', 'C', 'D', 'E', 'F'),
}


step = 0
def find_pos():
    for i in range(N):
        for j in range(M):
            if maze[i][j] == '0':
                sr, sc = i, j
                return sr, sc


sr, sc = find_pos()

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
visited = set()
def solve(r, c, dist):
    q = deque()
    q.append((r, c, [], 0))
    # 키여부에 따라 차원이 나뉨
    visited.add((r, c, tuple()))
    while q:  
        r, c, keys, step = q.popleft()
        for dir in range(4):
            nr, nc = r + dr[dir], c + dc[dir]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
        
            cell = maze[nr][nc]
        
            if cell == info['wall']:
                continue

            # 도착
            if cell == '1':
                return step + 1

            # 다음 키 상태 준비 (복사본 사용)
            nkeys = keys[:]  

            # 열쇠라면 획득 (소모 X)
            if cell in info['key']:
                if cell not in nkeys:
                    nkeys.append(cell)

            # 문이면 해당 키가 있어야 통과
            if cell in info['door']:
                need = cell.lower()
                if need not in nkeys:
                    continue

            state = (nr, nc, tuple(sorted(nkeys)))
            if state in visited:
                continue
            visited.add(state)
            q.append((nr, nc, nkeys, step + 1))

    return -1

print(solve(sr, sc, 0))