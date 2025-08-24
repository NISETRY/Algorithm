# 일단 간 다음에 벽 있는 개수를 count하고, 벽의 개수가 2개 이상인 경우는 걸러버리기
from collections import deque
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
que=deque([(0,0,1,k)]) # 시작점, 거리, 코인을 que에 넣고 시작
coin=k # 벽을 부숴버릴 수 있는 횟수, 딱코

# 우하좌상
dx=[1,0,-1,0]
dy=[0,1,0,-1]
ans=-1 # 경로 없을 시 답은 -1이니까 초기값을 이거로 설정

# 입력 받기, visited 만들기
zido=[list(input()) for _ in range(n)]
# 벽을 뚫은 세계관과 안뚫은 세계관은 다르다. 총 k+1개의 세계관 존재
# visited를 -1,0,1...k개로 세분화
# -1 : 미방문
# 나머지 : 방문 시 coin의 개수
visited = [[-1]*m for _ in range(n)]
visited[0][0]=k

for i in range(n):
    for j in range(m):
        zido[i][j]=int(zido[i][j])

# 문제점
# 벽을 만난 횟수를 카운트해야되는데, 이걸 어케함?
# 벽을 2번 만나는 경로를 자동종료하게 해야하는데 이게 문제

while que:
    x,y,dist,coin=que.popleft()
    if x==n-1 and y==m-1:
        ans=dist
        break
    for dir in range(4):
        nx,ny=x+dx[dir],y+dy[dir]
        if 0<=nx<n and 0<=ny<m:
            if zido[nx][ny] == 0:
                # 빈 칸: 코인 유지
                if coin>visited[nx][ny]:
                    visited[nx][ny] = coin
                    que.append((nx, ny, dist+1, coin))
            else:
                # 벽: 코인이 남아있을 때만 부수고 진행
                if coin > 0 and (coin-1)>visited[nx][ny]:
                    visited[nx][ny] = coin-1
                    que.append((nx, ny, dist+1, coin-1))

print(ans)