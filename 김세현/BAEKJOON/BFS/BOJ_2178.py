from collections import deque

i = 0
j = 0

def bfs(i, j, N, M):
    visited = [[0] * M for _ in range(N)]
    q = deque()    
    q.append([i,j])
    visited[i][j] = 1

    while q:
        ti, tj = q.popleft()

        if ti == N-1 and tj == M-1:
            return visited[ti][tj] 
        
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: 
            wi, wj = ti+di, tj+dj
            if 0<=wi<N and 0<=wj<M and miro[wi][wj] == 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1
    return 0

N, M = map(int, input().split())

miro = [list(map(int, input())) for _ in range(N)]
 
ans = bfs(i, j, N, M)

print(ans)

