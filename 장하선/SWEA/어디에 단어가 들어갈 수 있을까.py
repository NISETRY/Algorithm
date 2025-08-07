T=int(input())
for tc in range(1,T+1):
    n,k=map(int,input().split())
    matrix=[[0 for _ in range(n+2)] for _ in range(n+2)]
    res=0
    # input
    for i in range(n):
        matrix[i+1]=list(map(int,input().split()))
        matrix[i+1].append(0)
        matrix[i+1].insert(0,0)
    matrix[0]=[0 for _ in range(n+2)]
    matrix[n+1]=[0 for _ in range(n+2)]
    # 가로순회 : 1이 정확히 k개 연속된 거 세기
    for c in range(1,n+1):
        check=matrix[c]
        cnt=0
        for i in range(len(check)):
            if check[i]==1:
                cnt+=1
            else:
                if cnt==k:
                    res+=1
                    cnt=0
                    print(c, 'c')
                else:
                    cnt=0
    # 세로순회 : 행렬 뒤집고 위에 거 그대로
    for i in range(n+2):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for c in range(1,n+1):
        check=matrix[c]
        cnt=0
        for i in range(len(check)):
            if check[i]==1:
                cnt+=1
            else:
                if cnt==k:
                    res+=1
                    cnt=0
                    print(c, 'r')
                else:
                    cnt=0
    print(f'#{tc} {res}')