import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for _ in range(n):
    k=input().split()
    if k[0]=='push':
        stack.append(k[1])
    elif k[0]=='pop':
        print(stack.pop() if stack else -1)
    elif k[0]=='size':
        print(len(stack))
    elif k[0]=='empty':
        print(1 if not stack else 0)
    else:
        print(stack[-1] if stack else -1)