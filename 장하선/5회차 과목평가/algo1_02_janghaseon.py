T=int(input())
for tc in range(1,T+1):
    n,m=map(int, input().split())
    nums=list(map(int, input().split()))
    cnt=0
    for i in range(((n-1)//m)+1):
        # 슬라이싱
        if m*(i+1)<n:
            num_slice=nums[m*i:m*(i+1)]
        # 길이 안맞는 슬라이싱인 경우 끝까지
        else:
            num_slice=nums[m*i::]
        # flag 활용해서 감소혹은 유지되는 수열 나오면 안세줌
        flag=True
        if len(num_slice)==1:
            cnt+=1
        else:
            for i in range(len(num_slice)-1):
                if num_slice[i]>=num_slice[i+1]:
                    flag=False
                    break
            if flag:
                cnt+=1
    print(f'#{tc} {cnt}')
