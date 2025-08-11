n, m = map(int , input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
move = [[0,1],[1,0],[-1,0],[0,-1]]

temp = []

def comb(count):
    if count == 3:
        pick = temp[:]
        
        return

    for r in range(n):
        for c in range(m):
            if graph[r][c] == 0 and visited[r][c] == 0:
                temp.append([r,c])
                visited[r][c] = 1
                comb(count+1)
                a, b = temp.pop()
                visited[a][b] = 0

def bfs(a, b):
    pass
    # 바이러스 퍼져나가는 bfs 만들고
    

# 포문 돌면서 벽 세우고 바이러스면 bfs / safe_zone 구하기 끝
        