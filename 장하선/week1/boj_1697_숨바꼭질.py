from collections import deque
n,k=map(int,input().split())
cnt=0
visited=[0]*100001
nums=deque([n]) # 앞 요소 제거
visited[n]=1
while True:
    if n==k: # 같이 있으면 바로 찾으니 break
        break
    elif n>k: # 동생보다 수빈이가 앞에 있으면 뒤로 가는 거 말고 방법이 없음
        cnt=n-k
        break
    else:
        for _ in range(len(nums)):
            x=nums.popleft()
            if x==k:
                print(cnt)
                exit()
            for s in [x-1,x+1,2*x]:
                if 0<=s<=100000 and visited[s]==0:
                    visited[s]=1
                    nums.append(s)
        cnt+=1
print(cnt)