from collections import deque
n=int(input())
apt=[[0 for _ in range(n)] for _ in range(n)]
apt_nums=[] # 최종 출력
visited=[[False]*n for _ in range(n)]
visited[0][0]=True
queue=deque([(0,0)])
for i in range(n):
    k=input()
    for j in range(n):
        apt[i][j]=int(k[j])
# BFS로 접근, 1 나오면 상하좌우 검색해서 1인지 확인하고 1인거 안나올때까지 탐색
# 방문한거는 visited로 처리
# 주변에 0으로 둘러쌓였다->apt_nums에 붙은거 수 붙이기
dx=[-1,1,0,0]
dy=[0,0,-1,1]
while queue:
    x,y=queue.popleft()
    apt_nums.extend([0])
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and apt[nx][ny]==1:
                queue.append((nx,ny))
                apt_nums[-1]+=1
print(apt_nums)
