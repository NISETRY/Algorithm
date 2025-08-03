from collections import deque
n,m=map(int,input().split())
maze=[[] for _ in range(n)]
# 방문 표시 : maze와 같은 크기의 boolean 행렬인 visited를 만들어줌
visited = [[False]*m for _ in range(n)]
visited[0][0]=True
queue=deque([(0,0)])
for i in range(n):
    k=input()
    for j in range(m):
        maze[i].append(int(k[j]))
# 현 위치 x,y에 대해 이동 가능한 경우는 x+-1, y+-1 4개
# 막다른 길인 경우, pop으로 해당 리스트 반환 후 백트래킹
dx=[-1,1,0,0]
dy=[0,0,-1,1]
sc=0
while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if maze[nx][ny]!=0 and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny]=True
                    maze[nx][ny]=maze[x][y]+1
                    print(*queue)
print(maze[n-1][m-1])