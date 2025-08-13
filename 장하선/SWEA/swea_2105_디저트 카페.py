input()
for tc in range(1,11):
    dx=[1,1,-1,-1]
    dy=[1,-1,-1,1]
    n=int(input())
    dessert=[list(map(int,input().split()))for _ in range(n)]
    visited=[[False]*n for _ in range(n)]
    res=-1
    # dir로 방향 바꿔주는 경우 : 같은 수가 이미 나왔거나 경계에 닿았을 때
    # 출발점 : (0,0), (n-1,0), (0,n-1), (n-1,n-1)이 아닌 모든 지점
    # 시계/반시계 무관
    for i in range(n):
        for j in range(n):
            if not ((i==0 and j==0) or (i==0 and j==n-1) or (i==n-1 and j==n-1) or (i==n-1 and j==0)):
                dir=0
                while True:
                    nx,ny=i+dx[dir],j+dy[dir]