import math

def dfs(cnt,left,right):
    global ans
    # 가지치기 : 좌측이 과반 이상일때
    if left>tot_w/2:
        ans+=math.factorial(n-cnt)*2**(n-cnt)
        return
    # 다 놓았을떄
    if cnt==n:
        ans+=1
        return
    # 저울에 추를 놓는 로직
    for i in range(n):
        if visited[i]:
            continue
        visited[i]=1
        dfs(cnt+1,left+w[i],right)
        if right+w[i]<=left:
            dfs(cnt+1, left, right+w[i])
        visited[i]=0


T=int(input())
for tc in range(1,T+1):
    ans = 0
    n=int(input())
    w = list(map(int,input().split()))
    tot_w=sum(w)
    visited=[0]*n
    dfs(0,0,0)
    print(f'#{tc} {ans}')