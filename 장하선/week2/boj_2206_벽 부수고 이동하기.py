# 시작점 양 옆에 벽이 있으면 그건 무조건 부숴야됨
# 일단 간 다음에 벽 있는 개수를 count하고, 벽의 개수가 2개 이상인 경우는 걸러버리기
from collections import deque
n,m=map(int,input().split())
coin=1 # 벽을 부숴버릴 수 있는 횟수, 딱코
que=deque([(0,0)]) # 시작점을 que에 넣고 시작
# 우하좌상
dx=[1,0,-1,0]
dy=[0,1,0,-1]
# 입력 받기, visited 만들기
zido=[list(input()) for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        zido[i][j]=int(zido[i][j])

while que:
    x,y=que.popleft()
    for dir in range(4):
        nx,ny=x+dx[dir],y+dy[dir]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny]:
                if visited[nx][ny]==0:
                    que.append((nx,ny))
                else:
                    
