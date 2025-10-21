T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    k=n-m+1
    # 입력데이터
    plate = [list(map(int,input().split())) for _ in range(n)]
    # 필터
    filter = [list(map(int,input().split())) for _ in range(m)]
    # 합성곱 저장소
    conv = [[0]*k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            # 필터링 한 임시값 저장
            tmp=0
            for x in range(m):
                for y in range(m):
                    tmp+=plate[x+i][y+j]*filter[x][y]
            conv[i][j]=tmp
    print(f'#{tc}')
    for i in conv:
        print(*i)
    