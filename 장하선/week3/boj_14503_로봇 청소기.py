n,m=map(int,input().split())
r,c,d=map(int,input().split())
room=[list(map(int,input().split())) for _ in range(n)]
# 방문 안한 곳 = 청소 안한 곳, 방문한 곳 = 청소한 곳
visited=[[False for _ in range(m)]for _ in range(n)]
# 상우하좌
dx=[0,1,0,-1]
dy=[-1,0,1,0]
cnt=1
visited[r][c]=True
flag=True
def clean(x,y):
    global room
    global cnt
    if room[x][y]==0:
        visited[x][y]=True
        cnt+=1

def mode(x,y,dir):
    global flag
    if flag:
        for _ in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            dir=(dir-1)%4
            if room[nx][ny]==0 and not visited[nx][ny]:
                nx,ny=nx+dx[dir],ny+dy[dir]
                clean(nx,ny)
                mode(nx,ny,dir)
    # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        else:
            nd=(dir+2)%4
            if room[nx+dx[nd]][ny+dy[nd]]==0:
                nx,ny=nx+dx[nd],ny+dy[nd]
                clean(nx,ny)
                mode(nx,ny,dir)
            else:
                flag=False

mode(r,c,d)

print(cnt)