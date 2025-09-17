import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    synergy=[list(map(int,input().split()))for _ in range(n)]
    pick=[0 for _ in range(n)]
    flavor1=[]
    flavor2=[]
    temp=[]
    ans=float('inf')
    
    def yummy(flavor):
        tmp=0
        k=len(flavor)
        for i in range(k-1):
            a=flavor[i]
            for j in range(i+1,k):
                b=flavor[j]
                tmp+=synergy[a][b]+synergy[b][a]
        return tmp

    def comb(x):
        global ans
        if len(temp)==n//2:
            flavor1=temp[:]
            flavor2=[i for i in range(n) if not pick[i]]
            ans=min(ans, abs(yummy(flavor1)-yummy(flavor2)))
            return ans
                
        for i in range(x,n):
            if not pick[i]:
                temp.append(i)
                pick[i]=1
                comb(i+1)
                temp.pop()
                pick[i]=0

    comb(0)
    print(f'#{tc} {ans}')