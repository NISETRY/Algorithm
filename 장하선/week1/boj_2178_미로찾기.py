n,m=map(int,input().split())
maze=[[] for _ in range(n)]
visited=[[0,0]]
stack=[[0,0]]
for i in range(n):
    k=input()
    for j in range(m):
        maze[i].append(int(k[j]))
# 현 위치 x,y에 대해 이동 가능한 경우는 x+-1, y+-1 4개
# 이미 방문한 인덱스는 빈 리스트에 저장
# 막다른 길인 경우, pop으로 해당 리스트 반환 후 백트래킹
dx=[-1,1,0,0]
dy=[0,0,-1,1]
while stack:
    x,y=map(int, stack[-1])
    mv=False
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if maze[nx][ny]==1 and [nx, ny] not in visited:
            stack.append([nx,ny])
            visited.append([nx,ny])
            mv=True
            break
    if not mv:
        stack.pop()
print(len(visited))