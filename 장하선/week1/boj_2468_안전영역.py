from collections import deque
n=int(input())
safety_max=0
region=[[0] for _ in range(n)]
max_val=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    region[i]=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if region[i][j]>max_val:
            max_val=region[i][j]
for w in range(1,max_val+1):
    safety_region=[[0 for _ in range(n)] for _ in range(n)]
    visited=[[0 for _ in range(n)] for _ in range(n)]
    safety=0
    queue=deque()
    for i in range(n):
        for j in range(n):
            if region[i][j]>w:
                safety_region[i][j]=True
            else:
                safety_region[i][j]=False
                visited[i][j]=1
    for x in range(n):
        for y in range(n):
            if safety_region[x][y] and visited[x][y]==0:
                safety+=1
                queue.append((x,y))
                while queue:
                    for i in range(4):
                        queue.popleft()
                        nx,ny=x+dx[i],y+dy[i]
                        if 0<=nx<n and 0<=ny<n:
                            if safety_region[nx][ny]:
                                visited[nx][ny]=1
                                queue.append((x,y))
                        else:
                            break
                    break
                    # print(queue) # Debug
    print(w, safety)
    safety_max=max(safety_max, safety)
print(safety_max)