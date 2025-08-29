from collections import deque

# 벽 부수고 이동하기 풀이 1

def bfs(a,b):
    visited[a][b] = 0
    que = deque([(a,b,0)])
    dis = 0
    
    while que:
        dis += 1
        for _ in range(len(que)):
            x,y,broken = que.popleft()

            if x == n-1 and y== m-1:
                return dis

            for dx, dy in move:
                nx, ny = dx+x, dy+y

                if 0<=nx<n and 0<=ny<m:
                    if broken == 0 and graph[nx][ny] == 1 and visited[nx][ny] > broken:
                        visited[nx][ny] = broken+1
                        que.append((nx,ny,1))

                    if graph[nx][ny] == 0 and visited[nx][ny] > broken:
                        visited[nx][ny] = broken
                        que.append((nx,ny,broken))
    return -1


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[2]*m for _ in range(n)]
move = [[-1,0],[1,0],[0,1],[0,-1]]

print(bfs(0,0))

# 벽 부수고 이동하기 풀이 2

# def bfs(a,b):
#     visited[0][a][b] = 1
#     que = deque([(a,b,0)])

#     while que:
#         x,y,broken = que.popleft()
        
#         if x == n-1 and y == m-1:
#             return visited[broken][x][y]

#         for dx,dy in move:
#             nx,ny = dx+x, dy+y

#             if 0<=nx<n and 0<=ny<m:
#                 if graph[nx][ny] == 0 and visited[broken][nx][ny] == 0:
#                     visited[broken][nx][ny] = visited[broken][x][y] + 1
#                     que.append((nx,ny,broken))

#                 if graph[nx][ny] == 1 and visited[broken][nx][ny] == 0 and broken == 0:
#                     visited[broken+1][nx][ny] = visited[broken][x][y] + 1
#                     que.append((nx,ny,broken+1))

#     return -1

# n, m = map(int, input().split())
# graph = [list(map(int, input())) for _ in range(n)]
# visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
# move = [[-1,0],[1,0],[0,1],[0,-1]]

# print(bfs(0,0))