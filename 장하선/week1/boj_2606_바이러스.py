from collections import deque
n=int(input())
case=int(input())
com=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(case):
    a,b=map(int,input().split())
    com[a][b]=com[b][a]=1
visited=[1]
queue=deque([1])
while queue:
    x=queue.popleft()
    for i in range(1,n+1):
        if com[i][x]==1 and i not in visited:
            visited.append(i)
            queue.append(i)
print(len(visited)-1)