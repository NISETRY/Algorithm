from collections import deque
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    visited=[[False for _ in range(n)] for _ in range(n)]
    # 대각선 이동을 위한 델타
    dx=[-1,1,-1,1]
    dy=[-1,1,1,-1]
    dir=0
    queen=deque([(0,0)])
    visited[0][0]=True
    while queen:
        x,y=queen.pop()
        a,b=x,y
        for i in range(n):
            visited[x][i]=True
        for j in range(n):
            visited[j][y]=True
        while dir<4:
            nx,ny=x+dx[dir],y+dy[dir]
            visited[nx][ny]=True
            x,y=nx,ny
            if nx==0 or ny==0:
                dir+=1
                x,y=a,b
            if dir==4:
                dir=0
                break
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    queen.append((i,j))