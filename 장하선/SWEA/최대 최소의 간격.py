T=int(input())
for t in range(T):
    n=int(input())
    m=list(map(int,input().split()))
    a,i,ai,ii=0,11,-1,-1
    for x in range(n):
        if m[x]>=a:
            a,ai=m[x],x
        if m[x]<i:
            i,ii=m[x],x
    print(f'#{t+1} {abs(ai-ii)}')
