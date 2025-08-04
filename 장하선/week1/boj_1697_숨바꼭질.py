n,k=map(int,input().split())
cnt=0
nums=[n]
loc=[]
def w1(n):
    n-=1
    return n
def w2(n):
    n+=1
    return n
def tp(n):
    n*=2
    return n
while True:
    loc=nums
    nums.clear()
    cnt+=1
    for x in loc:
        nums.append(w1(x))
        nums.append(w2(x))
        nums.append(tp(x))
    if k in nums:
        break
print(cnt)