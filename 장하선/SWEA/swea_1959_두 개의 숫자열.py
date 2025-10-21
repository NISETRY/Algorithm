import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    num1=list(map(int,input().split()))
    num2=list(map(int,input().split()))
    if n>m:
        short,long=num2,num1
    else:
        short,long=num1,num2
    res=-9e10
    for i in range(abs(n-m)+1):
        tmp=0
        for j in range(min(n,m)):
            tmp+=short[j]*long[j+i]
        res=max(res,tmp)
    print(f'#{tc} {res}')