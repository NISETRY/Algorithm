import sys
sys.stdin=open('input.txt')

def dfs(node):
    for next in adj_list[node]:
        if visited[next]:
            continue
        visited[next]=1
        dfs(next)

T=int(input())
for tc in range(1,T+1):
    ans=0
    n,m=map(int,input().split())
    connent=list(map(int,input().split()))
    adj_list=[[] for _ in range(n+1)]
    visited=[0 for _ in range(n+1)]

    for i in range(m):
        idx1=i*2
        idx2=idx1+1
        adj_list[connent[idx1]].append(connent[idx2])
        adj_list[connent[idx2]].append(connent[idx1])
    for node in range(1,n+1):
        if visited[node]:
            continue

        ans+=1
        visited[node]=1
        dfs(node)

    print(f'#{tc} {ans}')