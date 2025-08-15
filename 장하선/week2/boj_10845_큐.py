import sys
input=sys.stdin.readline
n=int(input())
queue=[]
for _ in range(n):
    k=input().split()
    if k[0]=='push':
        queue.append(k[1])
    elif k[0]=='pop':
        print(queue.pop(0) if queue else -1)
    elif k[0]=='size':
        print(len(queue))
    elif k[0]=='empty':
        print(1 if not queue else 0)
    elif k[0]=='back':
        print(queue[-1] if queue else -1)
    else:
        print(queue[0] if queue else -1)