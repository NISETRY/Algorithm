T=int(input())
for tc in range(1,T+1):
    # 입력
    n,k=map(int,input().split())
    puzzle=[list(map(int,input().split()))for _ in range(n)]
    res=0
    
    # 행 검사
    for i in range(n):
        cnt=0
        for j in range(n):
            if puzzle[i][j]==1:
                cnt+=1
            else:
                if cnt==k:
                    res+=1
                cnt=0
        if cnt==k:
            res+=1
    # 열 검사
    for j in range(n):
        cnt=0
        for i in range(n):
            if puzzle[i][j]==1:
                cnt+=1
            else:
                if cnt==k:
                    res+=1
                cnt=0
        if cnt==k:
            res+=1
    print(f'#{tc} {res}')