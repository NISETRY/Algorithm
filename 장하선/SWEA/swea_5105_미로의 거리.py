# 우하좌상
from collections import deque
dx=[0,1,0,-1]
dy=[1,0,-1,0]
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    maze=[list(input()) for _ in range(n)]
    visited=[[False for _ in range(n)] for _ in range(n)]
    flag=False
    for i in range(n):
        for j in range(n):
            if maze[i][j]=='2':
                que=deque([(i,j)])
                visited[i][j]=True
                break
    while que and not flag:
        x,y=que.popleft()
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if 0<=nx<n and 0<=ny<n:
                if maze[nx][ny]=='0' and not visited[nx][ny]:
                    que.append((nx,ny))
                    visited[nx][ny]=True
                    maze[nx][ny]=int(maze[x][y])+1
                if maze[nx][ny]=='3':
                    flag=True
                    break       
    if flag:
        print(f'#{tc} {maze[x][y]-2}')
    else:
        print(f'#{tc} {0}')
