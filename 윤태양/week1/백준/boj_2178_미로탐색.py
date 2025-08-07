n ,m = map(int, input().split())

graph = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

for i in range(n):
    temp = list(map(int, input()))
    for j in range(m):
        graph[i][j] = temp[j]

move = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(a,b):
    visited[a][b] = 1
    que = []
    que.append([a,b])

    while que:
        x, y = que.pop(0)
        if x == n-1 and y == m-1:
            print(visited[x][y])
            return

        for i,j in move:
            if 0<=x+i<=n-1 and 0<=y+j<=m-1:
                if graph[x+i][y+j] == 1 and visited[x+i][y+j] == 0:
                    que.append([x+i, y+j])
                    visited[x+i][y+j] = visited[x][y] + 1

bfs(0,0)