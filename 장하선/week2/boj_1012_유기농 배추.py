from collections import deque
# 우좌하상
dx = [1,-1,0,0]
dy = [0,0,1,-1]
res=0
# 입력
T=int(input())
for tc in range(T):
    m,n,k=map(int,input().split())
    farm=[[0 for _ in range(n)]for _ in range(m)]
    zilung=[]
    for _ in range(k):
        i,j=map(int,input().split())
        farm[i][j]=1
        zilung.append([i,j])
    bugs=0
    while bugs<k:
        x,y=zilung.pop()
        farm[x][y]=0
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if [nx,ny] in zilung:
                zilung.remove([nx,ny])
            x,y=nx,ny
            break