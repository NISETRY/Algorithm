from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
spots=[[] for _ in range(n+1)]
cnt=0
for _ in range(m):
    a,b=map(int,input().split())
    spots[a].append(b)
    spots[b].append(a)
# 1부터 시작
visited=[0 for _ in range(n+1)]
queue=deque()
def bfs(start):
    global visited
    visited[start]=1
    queue.append(start)
    while queue:
        x=queue.popleft()
        for i in spots[x]:
            if visited[i]==0:
                visited[i]=1
                queue.append(i)
    return 1
for i in range(1,n+1):
    if visited[i]==0:
        cnt+=bfs(i)
print(cnt)