T=int(input())
for t in range(1,T+1):
    n,m=map(int, input().split())
    min_num=999999999
    max_num=-999999999
    nums=list(map(int, input().split()))
    for i in range(n-m+1):
        sums=0
        for j in range(i,1+m):
            sums+=nums[j]
        if sums<min_num:
            min_num=sums
        if sums>max_num:
            max_num=sums
    print(f'#{t} {max_num-min_num}')