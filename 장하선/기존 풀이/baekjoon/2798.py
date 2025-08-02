n,m=map(int, input().split())
cards=list(map(int, input().split()))
cards.sort()
res=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            nums=cards[i]+cards[j]+cards[k]
            if nums>m:
                continue
            else:
                res=max(res,nums)
print(res)