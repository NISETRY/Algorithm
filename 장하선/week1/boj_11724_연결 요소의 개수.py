from collections import deque
n,m=map(int,input().split())
spots=[[0 for _ in range(n+1)] for _ in range(n+1)]
dots=[i+2 for i in range(n-1)]
cnt=0
for _ in range(m):
    a,b=map(int,input().split())
    spots[a][b]=spots[b][a]=1
visited=[]
queue=deque([1])
while dots:
    while queue:
        x=queue.popleft()
        try:
            for i in range(1,n+1):
                if spots[i][x]==1 and i not in visited:
                    visited.append(i)
                    queue.append(i)
                    dots.remove(i)
        except ValueError:
            break
    cnt+=1
print(cnt)