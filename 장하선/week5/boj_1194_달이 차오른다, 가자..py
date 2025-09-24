from collections import deque
import sys
input=sys.stdin.readline
# 상하좌우 델타
dr=[0,0,-1,1]
dc=[-1,1,0,0]
n,m=map(int,input().split())
moon=[list(input().strip()) for _ in range(n)]
visited=[[[0]*64 for _ in range(m)] for _ in range(n)]
key_caught=0
flag=True
for i in range(n):
    for j in range(m):
        if moon[i][j]=='0':
            queue=deque([(i,j,0,key_caught)])
            visited[i][j][key_caught]=1
            break
while queue:
    r,c,cnt,keys=queue.popleft()
    if moon[r][c]=='1':
        print(cnt)
        sys.exit(0)
    if flag:
        for d in range(4):
            nr,nc=r+dr[d], c+dc[d]
            if not (0<=nr<n and 0<=nc<m):
                continue
            loc=moon[nr][nc]
            if loc=='#':
                continue
            nkey=keys
            if 'a'<=loc<='f':
                bit=1<<(ord(loc)-ord('a'))
                nkey=keys|bit
            elif 'A'<=loc<='F':
                stat=1<<(ord(loc)-ord('A'))
                if keys&stat==0:
                    continue
            if visited[nr][nc][nkey]:
                continue
            visited[nr][nc][nkey]=1
            queue.append((nr,nc,cnt+1,nkey))
print(-1)