T=int(input())
for tc in range(1,T+1):
    n=int(input())
    apple=[[] for _ in range(n)]
    for i in range(n):
        x,y=map(int,input().split())
        apple[i]=(x,y)
    # 사과 간 거리를 모두 저장
    # 시작, 끝은 모두 (0,0)
    res=999999999
    loc=[(0,0)]
    # 순열로 모든 경우의 수를 뽑음(pruning은 시간 관계상..)
    def perm():
        global res
        if len(loc)==n+1:
            distance=0
            for i in range(n):
                distance+=abs(loc[i+1][0]-loc[i][0])+abs(loc[i+1][1]-loc[i][1])
            # 마지막 돌아오는 거리 더함
            distance+=loc[-1][0]+loc[-1][1]
            # 최솟값으로 최신화
            if distance<res:
                res=distance
            return
        for i in range(n):
            if apple[i] not in loc:
                loc.append(apple[i])
                perm()
                loc.pop()
    perm()
    print(f'#{tc} {res}')