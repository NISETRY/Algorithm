from collections import deque

import sys
T = int(sys.stdin.readline())
que = deque()
for i in range(T):
    command = sys.stdin.readline().strip()
    if command.startswith('push'):
        word, num = command.split()
        que.append(num)
    elif command == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif command == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif command == 'size':
        print(len(que))
    elif command == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
    elif command == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])