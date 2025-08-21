from collections import deque
for tc in range(1,11):
    input()
    nums=deque(map(int,input().split()))
    flag=True
    while flag:
        for i in range(1,6):
            if nums[-1]<=0:
                flag=False
                break
            x=nums.popleft()
            nums.append(x-i)  
    nums[-1]=0
    print(f'#{tc}', end=' ')
    print(*nums)