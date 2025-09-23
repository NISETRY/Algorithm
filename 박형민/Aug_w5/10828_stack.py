import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    
    raw = sys.stdin.readline().split()
    txt = raw[0]

    if "push" in raw:
        stack.append(raw[1])
        
    elif "pop" == txt:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif "size" == txt:
        print(len(stack))


    elif "empty" == txt:
        if stack:
            print(0)
        else:
            print(1)

    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)