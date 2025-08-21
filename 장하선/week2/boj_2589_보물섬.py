from collections import deque
n,m=map(int,input().split())
treasure=[list(input()) for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]
# 우하좌상
dx=[0,1,0,-1]
dy=[1,0,-1,0]
max_dis=0
# Land 방문 후 거리 구하기
# 생각해보니 visited 초기화가 시작 지점별로 진행되어야 할 것 같다
land_list=[]
for i in range(n):
    for j in range(m):
        if treasure[i][j]=='L':
            land_list.append([i,j])
for loc in land_list:
    i,j=loc[0].loc[1]
    visited[i][j]=True
    queue=deque([(i,j)])
    cnt=0
    while queue:
        x,y=queue.popleft()
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and treasure[nx][ny]=='L':
                    visited[nx][ny]=True
                    x,y=nx,ny
                    cnt+=1
                    queue.append((nx,ny))


print(max_dis)
