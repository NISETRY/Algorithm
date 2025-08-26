n,m=map(int,input().split())
r,c,d=map(int,input().split())
room=[list(map(int,input().split())) for _ in range(n)]
# 방문 안한 곳 = 청소 안한 곳, 방문한 곳 = 청소한 곳
visited=[[False for _ in range(m)]for _ in range(n)]
# 상우하좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]
cnt=1
visited[r][c]=True

# 청소하는 함수, (x,y)가 청소되었다면 visited[x][y]=True하고 청소한 칸의 개수 카운팅
def clean(x,y):
    global room, cnt
    if room[x][y]==0:
        visited[x][y]=True
        cnt+=1

def mode(x,y,dir):
    # 1. 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    for _ in range(4):
        # 반시계 방향으로 회전
        dir=(dir-1)%4
        nx,ny=x+dx[dir],y+dy[dir]
        # 경계에 가지 않고, 벽이 아니면서 청소하지 않은 칸인 경우
        if 0<=nx<n and 0<=ny<m and room[nx][ny]==0 and not visited[nx][ny]:
            # 전진할 칸 방문 처리
            clean(nx,ny)
            # 전진하고 방향 전환
            return nx,ny,dir,False
        
    # 2. 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    # 후진을 위한 새로운 dir 선언
    nd=(dir+2)%4
    mx,my=x+dx[nd],y+dy[nd]
    # 후진이 가능하다면
    if 0<=mx<n and 0<=my<m and room[mx][my]==0:
        # 후진
        return mx,my,dir,False
    # 후진이 불가능하면 그 자리에서 멈추고 로직 종료
    else:
        return x,y,dir,True

while True:
    # stop이 True면 계속 진행
    r,c,d,stop=mode(r,c,d)
    # 멈추면 끝
    if stop:
        break

print(cnt)