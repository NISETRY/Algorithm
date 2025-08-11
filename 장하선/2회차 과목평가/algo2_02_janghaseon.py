T=int(input())

for tc in range(1,T+1):
    n,m=map(int, input().split())
    # 입력 받기
    region=[[0] for _ in range(n)]
    for i in range(n):
        region[i]=list(map(int, input().split()))
    # 확인을 위해 델타 사용
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    safe=0 # 안전구역 수를 저장할 변수 선언
    # 가생이 제외한 나머지만 확인
    for x in range(1,n-1):
        for y in range(1,m-1):
            # 확인할 위치를 check로 변수 선언
            check=region[x][y]
            for d in range(4):
                # flag 선언해서 주변 조건을 다 확인하고 안전지대인 경우만 safe 변수 count
                flag=True
                nx,ny=x+dx[d],y+dy[d]
                if check<region[nx][ny]:
                    # 더 높은 지역이 있으면 확인할 필요 없다.
                    flag=False
                    break
            if flag:
                safe+=1
    print(f'#{tc} {safe}')