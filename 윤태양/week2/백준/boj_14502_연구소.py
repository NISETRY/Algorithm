n, m = map(int , input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [[0,1],[1,0],[-1,0],[0,-1]]
zeros = [(r, c) for r in range(n) for c in range(m) if graph[r][c] == 0]
# 인풋 받기
temp = []
pick = []
def comb(count, idx):
    if count == 3:
        pick.append(temp[:])
        return

    for i in range(1, len(zeros)+1):
        a, b = zeros[i-1]
        if i> idx:
            temp.append([a,b])
            comb(count+1, i)
            temp.pop()
# 벽 조합 생성
def bfs(a, b):
    visited[a][b] = 1
    que = [[a,b]]
    cnt = 0

    while que:
        a, b = que.pop(0)
        for i, j in move:
            nx, ny = a+i, b+j
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    que.append([nx,ny])
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt
# 바이러스 bfs생성
comb(0,0)

virus = []  
safe = 0  
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append([i,j])
        if graph[i][j] == 0:
            safe += 1    
# safe 개수, virus 인덱스 찾기
ans = 0

for a, b, c in pick:
    graph[a[0]][a[1]] = 1   # 벽 세우기
    graph[b[0]][b[1]] = 1
    graph[c[0]][c[1]] = 1

    visited = [[0]*m for _ in range(n)] # bfs용 visited 초기화
    test_safe = safe                    # safe 초기화
    kill = 0                            # 킬 초기화
    for k, v in virus:                  # 바이러스 영역 bfs
        kill += bfs(k,v)

    graph[a[0]][a[1]] = 0   # 벽 허물기
    graph[b[0]][b[1]] = 0
    graph[c[0]][c[1]] = 0

    ans = max(ans, test_safe-kill-3) # 벽 개수(3)은 빼줘야 한다

print(ans)

        