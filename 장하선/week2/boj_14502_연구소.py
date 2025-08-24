import copy
from collections import deque
n,m=map(int,input().split())
ori_virus=[list(map(int,input().split())) for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
res=0
covid=[]
# 값이 0인 모든 곳은 잠재적인 벽 세울 수 있는 후보지
# 일단 벽을 세우고 바이러스 퍼진 후 결과 확인하고 max와 비교?
cand=[]
for i in range(n):
    for j in range(m):
        if ori_virus[i][j]==0:
            cand.append((i,j))
        elif ori_virus[i][j]==2:
            covid.append((i,j))
l=len(cand)
# i,j,k : 벽의 위치
virus=copy.deepcopy(ori_virus)
for i in range(l-2):
    for j in range(i+1,l-1):
        for k in range(j+1,l):
            virus[cand[i][0]][cand[i][1]]=1
            virus[cand[j][0]][cand[j][1]]=1
            virus[cand[k][0]][cand[k][1]]=1
            # 벽을 만들어준 후 바이러스 전이 확인
            for x,y in covid:
                que=deque([(x,y)])
                while que:
                    xi,yi=que.popleft()
                    for d in range(4):
                        nx,ny=xi+dx[d],yi+dy[d]
                        if 0<=nx<n and 0<=ny<m and virus[nx][ny]==0:
                            virus[nx][ny]=2
                            que.append((nx,ny))
            # 전이 확인이 끝났으면 안전구역 확인
            cnt=0
            for a in range(n):
                for b in range(m):
                    if virus[a][b]==0:
                        cnt+=1
            res=max(res,cnt)
            virus=copy.deepcopy(ori_virus) # 초기화
print(res)