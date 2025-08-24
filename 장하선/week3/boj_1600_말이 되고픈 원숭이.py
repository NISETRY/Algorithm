from collections import deque
k=int(input())
w,h=map(int, input().split())
zido=[list(map(int, input().split())) for _ in range(h)]
# -1 : 쌩으로 방문 안함, 나머지 방문 경우는 cnt 값을 visited에 채워줌
visited = [[-1]*w for _ in range(h)]
# 불능해를 초기 값으로 setting
res=-1
# 델타 1. 날으는쌀숭이
horse_x=[1,1,2,2,-1,-1,-2,-2]
horse_y=[2,-2,1,-1,2,-2,1,-1]
# 델타 2. 그냥 쌀숭이 / 우하좌상
dx=[1,0,-1,0]
dy=[0,1,0,-1]

# queue에 넣는 것 : x,y 좌표, 이동거리, k
queue=deque([(0,0,0,k)])

# 이동 방식에 따라 함수 설정
def walk(x,y):
    global queue
    global visited
    for dir in range(4):
        nx,ny=x+dx[dir],y+dy[dir]
        if 0<=nx<h and 0<=ny<w and zido[nx][ny]==0:
            if cnt>visited[nx][ny]:
                visited[nx][ny]=cnt
                queue.append((nx,ny,dist+1,cnt))

def horse(x,y):
    global queue
    global visited
    global cnt
    if cnt==0:
        return
    for dir in range(8):
        nx,ny=x+horse_x[dir],y+horse_y[dir]
        if 0<=nx<h and 0<=ny<w and zido[nx][ny]==0:
            if cnt-1>visited[nx][ny]:
                visited[nx][ny]=cnt-1
                queue.append((nx,ny,dist+1,cnt-1))

while queue:
    x,y,dist,cnt=queue.popleft()
    if x==h-1 and y==w-1:
        res=dist
        break
    # k=0이면 델타 2로만 이동 가능
    if cnt==0:
        walk(x,y)
    else:
    # 델타 1,2로 이동 가능한 모든 경우의 수 queue에 저장
        walk(x,y)
        horse(x,y)

print(res)