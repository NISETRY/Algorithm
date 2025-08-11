from collections import deque
n=int(input())
apt=[[0 for _ in range(n)] for _ in range(n)]
apt_nums=[] # 최종 출력
visited=[[False]*n for _ in range(n)]
# 입력 처리
for i in range(n):
    k=input()
    for j in range(n):
        apt[i][j]=int(k[j])
# BFS로 접근, 1 나오면 상하좌우 검색해서 1인지 확인하고 1인거 안나올때까지 탐색
# 방문한거는 visited로 처리
# 주변에 0으로 둘러쌓였다->apt_nums에 붙은거 수 붙이기
dx=[-1,1,0,0]
dy=[0,0,-1,1]
# 아파트 있는 부분만 반복문 돌고 단지에 포함시키기
for i in range(n):
    for j in range(n):
        if apt[i][j]==1 and not visited[i][j]:
            queue=deque([(i,j)])
            visited[i][j]=True
            cnt=1
            while queue:
                x,y=queue.popleft()
                for d in range(4):
                    nx,ny=x+dx[d],y+dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if apt[nx][ny]==1 and not visited[nx][ny]:
                            queue.append((nx,ny))
                            visited[nx][ny]=True
                            cnt+=1
            apt_nums.append(cnt)

# 정답 출력 처리            
apt_nums.sort()
d=len(apt_nums)
print(d)
for i in range(d):
    print(apt_nums[i])