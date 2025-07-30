T=int(input())
for t in range(1,T+1):
    n=int(input())
    farm=[[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        k=input()
        for j in range(len(k)):
            farm[i][j]=int(k[j]) #농장 생성
    val=0
    for i in range(n):
        if n//2-i>0:
            val+=sum(farm[i][n//2-i:n//2+i+1])
        else:
            val+=sum(farm[i][n//2-(n-1-i):n//2+(n-1-i)+1])
    print(f'#{t} {val}')