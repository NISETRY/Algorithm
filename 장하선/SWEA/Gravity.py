T=int(input())
for t in range(1, T+1):
    n=int(input())
    z=list(map(int, input().split()))
    max_drop=0
    for i in range(n):
        drop=0
        for j in range(i+1, n):
            if z[j]<z[i]:
                drop+=1
        if drop>max_drop:
            max_drop=drop
    print(f'#{t} {max_drop}')