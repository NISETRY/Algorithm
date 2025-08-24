from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
treasure=[list(input()) for _ in range(n)]
res=0
# 우하좌상
dx=[0,1,0,-1]
dy=[1,0,-1,0]
# Land 방문 후 거리 구하기
# 생각해보니 visited 초기화가 시작 지점별로 진행되어야 할 것 같다

# 1차 답 : 8 안나오고 10 나옴
# 이유 추측 : 지도 상에서 8로 갈 수 있는거를 돌아가서 10이 나온듯
# BFS로 가장 먼 거리 탐색은 성공했으나, 그걸 그렇다고 진짜 가장 멀게 가버려서 문제

# 1차 제출 : 시간초과
# bfs 과정을 함수로 바꿔서 재시도
# testcase 맞았는데 틀렸다
# 는 이거 랜덤생성이구나 앞으로 2번 돌려야지...
# 시작점 방문처리 안해서 fail나옴

def bfs(i,j):
    max_dis=0
    queue=deque([(i,j,0)])
    visited=[[False for _ in range(m)] for _ in range(n)]
    visited[i][j]=True
    while queue:
        x,y,dist=queue.popleft()
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if treasure[nx][ny]=='L':
                    visited[nx][ny]=True
                    queue.append((nx,ny,dist+1))
        max_dis=max(max_dis,dist)
    return max_dis

for i in range(n):
    for j in range(m):
        if treasure[i][j]=='L':
            res=max(res,bfs(i,j))
print(res)
