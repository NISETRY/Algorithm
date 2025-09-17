import sys
sys.stdin=open('input.txt')

from collections import deque
# 상하좌우
dr=[-1,1,0,0]
dc=[0,0,-1,1]
# 터널 유형에 따른 이동 가능한 경로
def move(x):
    if x==1: return (0,1,2,3)
    elif x==2: return (0,1)
    elif x==3: return (2,3)
    elif x==4: return (0,3)
    elif x==5: return (1,3)
    elif x==6: return (1,2)
    else: return (0,2)

opp={0:1,1:0,2:3,3:2}

T=int(input())
for tc in range(1,T+1):
    n,m,r,c,l=map(int,input().split())
    # 위치정보, 이동칸수 저장
    queue=deque([(r,c,0)])
    itachi=[list(map(int,input().split())) for _ in range(n)]
    # 시작 지점이 0이면 돌 필요가 없다
    if itachi[r][c]==0:
        print(f'{tc} 0')
        continue
    visited=[[0 for _ in range(m)]for _ in range(n)]
    # 시작 지점 방문처리
    visited[r][c]=1
    ans=1
    while queue:
        x,y,dist=queue.popleft()
        if dist==l-1:
            continue
        for j in move(itachi[x][y]):
            nr,nc=x+dr[j],y+dc[j]
            if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
                if itachi[nr][nc]==0:
                    continue
                if opp[j] in move(itachi[nr][nc]):
                    visited[nr][nc]=1
                    queue.append((nr,nc,dist+1))
                    ans+=1
    print(f'#{tc} {ans}')