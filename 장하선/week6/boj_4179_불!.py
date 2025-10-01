# 상하좌우
import sys
input=sys.stdin.readline
from collections import deque
dr=[0,0,-1,1]
dc=[-1,1,0,0]
r,c=map(int,input().split())
maze=[list(input().strip()) for _ in range(c)]
visited=[[[[0 for _ in range(r)] for _ in range(c)] for _ in range(r)] for _ in range(c)]
jfind, ffind=False, False
for i in range(c):
    for j in range(r):
        if maze[i][j]=='J':
            jfind=True
            jr,jc=i,j
            break
        if maze[i][j]=='F':
            ffind=True
            fr,fc=i,j
            break
    if jfind and ffind:
        break
queue=deque([(jr,jc,fr,fc)])
res=987654321
flag=False
while queue:
    jr,jc,fr,fc=queue.popleft()
    

print(res if flag else 'IMPOSIIBLE')