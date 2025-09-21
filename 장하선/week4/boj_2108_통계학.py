n=int(input())
nums=[0]*n
sums=0
cnts=[0]*8001
max_val=-4001
min_val=4001
for i in range(n):
    tmp=int(input())
    nums[i]=tmp
    sums+=tmp
    cnts[tmp+4000]+=1
    max_val=max(tmp,max_val)
    min_val=min(tmp,min_val)

nums.sort()
print(round(sums/n))
print(nums[n//2])
freq = max(cnts)
modes = [i-4000 for i,v in enumerate(cnts) if v==freq]
modes.sort()
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])
print(max_val-min_val)