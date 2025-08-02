start, x=map(int, input().split())
nums=[start]
new=0
while True:
    if new in nums[0:len(nums)-1]:
        break
    new=0
    for i in range(len(str(start))):
        new+=int(str(start)[i])**x
    nums.append(new)
    start=new
idx=nums.index(nums[-1])
print(idx)