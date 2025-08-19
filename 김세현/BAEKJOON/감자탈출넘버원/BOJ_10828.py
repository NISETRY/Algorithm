import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    st = sys.stdin.readline().split()
    order = st[0]

    if order == "push":
        stack.append(int(st[1]))  # 숫자로 변환 (필수는 아니지만 권장)

    elif order == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif order == "size":
        print(len(stack))

    elif order == "empty":
        print(0 if stack else 1)

    elif order == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
