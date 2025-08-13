input()
def tour(x,y,dir):
    temp=1
    cnt=[dessert[x][y]]
    a,b=x,y
    while True:
        nx,ny=x+dx_1[dir],y+dy_1[dir]
        if nx==a and ny==b: # 기본 탈출조건
            return temp if temp>=4 else -1
        if not (0<=nx<n and 0<=ny<n) or dessert[nx][ny] in cnt:
            dir+=1
            if dir==4: # 다 못돌아도 탈출
                return -1
            continue
        x,y=nx,ny
        cnt.append(dessert[x][y])
        temp+=1

for tc in range(1,11):
    dx_1=[1,1,-1,-1]
    dy_1=[1,-1,-1,1]
    n=int(input())
    dessert=[list(map(int,input().split()))for _ in range(n)]
    res=-1
    # dir로 방향 바꿔주는 경우 : 같은 수가 이미 나왔거나 경계에 닿았을 때
    # 출발점 : (0,0), (n-1,0), (0,n-1), (n-1,n-1)이 아닌 모든 지점
    # 시계/반시계 무관
    for i in range(n):
        for j in range(n):
            if not ((i==0 and j==0) or (i==0 and j==n-1) or (i==n-1 and j==n-1) or (i==n-1 and j==0)):
                val=tour(i,j,0)
                res=max(res,val)
    print(f'#{tc} {res}')
                    
