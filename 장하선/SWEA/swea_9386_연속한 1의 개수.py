T=int(input())
for tc in range(1,T+1):
    max_val=0
    n=int(input())
    nums=input()
    temp=0
    for i in range(n):
        if nums[i]=='1':
            temp+=1
            if i==n-1:
                max_val=max(temp,max_val)
        if nums[i]=='0':
            max_val=max(temp,max_val)
            temp=0
    print(f'#{tc} {max_val}')