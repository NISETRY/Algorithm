from collections import deque
n=int(input())
safety_max=0 # 답으로 출력할 변수
region=[[0] for _ in range(n)]
max_val=0 # 최대 물 높이
# delta
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    region[i]=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if region[i][j]>max_val:
            max_val=region[i][j]

# 본 로직
for w in range(max_val+1):
    visited=[[False]*n for _ in range(n)] # visited 선언
    safety=0 # 생존구역의 넓이
    for i in range(n):
        for j in range(n):
            if region[i][j]>w and not visited[i][j]:
                safety+=1 # 생존구역인 경우 너비 +1
                queue=deque([(i,j)]) # BFS 탐색 준비
                visited[i][j]=True # 방문 처리
                while queue:
                    x,y=queue.popleft()
                    # 상/하/좌/우로 안잠겼고, 방문 안헀을 때 방문 진행
                    for d in range(4):
                        nx,ny=x+dx[d],y+dy[d]
                        if 0<=nx<n and 0<=ny<n:
                            if region[nx][ny]>w and not visited[nx][ny]:
                                queue.append((nx,ny))
                                visited[nx][ny]=True
    # 생존구역 넓이 최댓값 갱신
    safety_max=max(safety_max, safety)
print(safety_max)