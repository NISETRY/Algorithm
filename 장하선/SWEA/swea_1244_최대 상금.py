# 값 나온 것을 비교하기 위한 계산기
def calc(nums):
    ans=0
    for i in range(ln):
        ans+=nums[i]*(10**(ln-1-i))
    return ans
    
def dfs(cnt):
    # 비교 횟수 다 소진하면 retrun
    global res
    if cnt==max_cnt:
        res=max(res, calc(nums))
        return
    # 교환 로직
    for x in range(ln-1):
        for y in range(x+1, ln):
            nums[x], nums[y]=nums[y], nums[x]
            tmp=calc(nums)
            if (cnt, tmp) not in check:
                dfs(cnt+1)
                check.append((cnt,tmp))
            nums[y], nums[x]=nums[x], nums[y]          
                                
T=int(input())
for tc in range(1, T+1):
    nums, max_cnt = input().split()
    max_cnt=int(max_cnt)
    # 기본값 : 원래 주어진 input값
    res=0
    nums=list(nums)
    ln=len(nums)
    check=[]
    for i in range(ln):
        nums[i]=int(nums[i])
    dfs(0)
    print(f'#{tc} {res}')