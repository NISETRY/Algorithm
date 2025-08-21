# 우하좌상
from collections import deque
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for tc in range(1,11):
    input()
    maze=[list(input()) for _ in range(16)]
    visited=[[False for _ in range(16)] for _ in range(16)]
    res=0
    flag=False
    # print(visited)
    for i in range(16):
        for j in range(16):
            if maze[i][j]=='2':
                que=deque([(i,j)])
                visited[i][j]=True
                break
    while que and not flag:
        x,y=que.popleft()
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if 0<=nx<16 and 0<=ny<16:
                if maze[nx][ny]=='0' and not visited[nx][ny]:
                    que.append((nx,ny))
                    visited[nx][ny]=True
                if maze[nx][ny]=='3':
                    res=1
                    flag=True
                    break
        print(que)
    print(f'#{tc} {res}')
