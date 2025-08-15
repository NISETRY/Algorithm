T=int(input())
def cross(x,y,m): # x,y : 약 뿌리는 지점
    dx=[0,1,0,-1]
    dy=[-1,0,1,0]
    res=flies[x][y]
    for i in range(1,m):
        for j in range(4):
            nx=x+dx[j]*i
            ny=y+dy[j]*i
            if 0<=nx<n and 0<=ny<n:
                res+=flies[nx][ny]
    return res
def x_shape(x,y,m): # x,y : 약 뿌리는 지점
    dx=[1,1,-1,-1]
    dy=[1,-1,1,-1]
    res=flies[x][y]
    for i in range(1,m):
        for j in range(4):
            nx=x+dx[j]*i
            ny=y+dy[j]*i
            if 0<=nx<n and 0<=ny<n:
                res+=flies[nx][ny]
    return res
for tc in range(1,T+1):
    n,m=map(int,input().split())
    flies=[[0] for _ in range(n)]
    max_val=0
    for x in range(n):
        lst=list(map(int,input().split()))
        flies[x]=lst
    for i in range(n):
        for j in range(n):
            fly_1=cross(i,j,m)
            fly_2=x_shape(i,j,m)
            max_val=max(max_val,fly_1,fly_2)
    print(f'#{tc} {max_val}')