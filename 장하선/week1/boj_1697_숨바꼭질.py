from collections import deque
n,k=map(int,input().split())
cnt=0
visited=[0]*100001
nums=deque([n]) # 앞 요소 제거
loc=deque() # 현재 위치 후보 짬통
def walk_1(n): # 걷기 1
    return n-1
def walk_2(n): # 걷기 2
    return n+1
def tp(n): # 텔포
    return n*2
while k not in loc:
    if n==k: # 같이 있으면 바로 찾으니 break
        break
    if n>k: # 동생보다 수빈이가 앞에 있으면 뒤로 가는 거 말고 방법이 없음
        cnt=n-k
        break
    for _ in range(len(nums)): # 수빈아 뒤질래??
        x=nums.popleft()

    
print(cnt)