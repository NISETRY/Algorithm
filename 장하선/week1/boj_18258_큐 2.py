import sys
from collections import deque
input=sys.stdin.readline

que=deque()
def q(cmd):
    global que   
    if cmd[0]=='push':
        que.append(int(cmd[1]))
    elif cmd[0]=='pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif cmd[0]=='size':
        print(len(que))
    elif cmd[0]=='empty':
        print(0 if que else 1)
    elif cmd[0]=='front':
        print(que[0] if que else -1)
    elif cmd[0]=='back':
        print(que[-1] if que else -1)
n=int(input())
for _ in range(n):
    cmd=input().split()
    q(cmd)