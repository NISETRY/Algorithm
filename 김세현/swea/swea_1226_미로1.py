#시작점 찾기
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                return i, j

def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    q = []    
    q.append([i,j])
    visited[i][j] = 1

    while q:
        ti, tj = q.pop(0)
        if maze[ti][tj] == 2:
            return 1 
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: 
            wi, wj = ti+di, tj+dj
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1
    return 0

for tc in range(1, 11):
     
    N = 16
    input()
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N) 
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')
