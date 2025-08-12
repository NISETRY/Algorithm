T=int(input())
for tc in range(1,T+1):
    n,m,c=map(int, input().split())
    honeycomb=[list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n-m+1):
            honey_1=honeycomb[i][j:j+m]
            