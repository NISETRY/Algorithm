from collections import deque
n,m=map(int,input().split())
box=[list(map(int,input().split())) for _ in range(m)]

# 우하좌상
res=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 초기 토마토가 2개 이상이다 -> 하루에 여러 군데에서 1 증가
queue=deque([])
for i in range(m):
    for j in range(n):
        if box[i][j]==1:
            queue.append([i,j])
while queue:
    x,y=queue.popleft()
    for dir in range(4):
        nx,ny=x+dx[dir],y+dy[dir]
        if 0<=nx<m and 0<=ny<n:
            if box[nx][ny]==0:
                box[nx][ny]=box[x][y]+1
                queue.append((nx,ny))

# 출력 양식
for i in range(m):
    if 0 in box[i]:
        print(-1)
        break
    max_val=max(box[i])
    res=max(res,max_val)
else:
    print(res-1)