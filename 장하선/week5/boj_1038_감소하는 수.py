n=int(input())
nums=[]
for mask in range(1,1<<10):
    sub=[]
    for i in range(9,-1,-1):
        if mask&(1<<i):
            sub.append(str(i))
    nums.append(int(''.join(sub)))
nums.sort()
print(nums[n] if n<1023 else -1)