from collections import deque

import sys
T = int(sys.stdin.readline())
deque = deque()
for i in range(T):
    command = sys.stdin.readline().strip()
    if command.startswith('push_front'):
        word, num = command.split()
        deque.appendleft(num)
    elif command.startswith('push_back'):
        word, num = command.split()
        deque.append(num)    
    elif command == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif command == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif command == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command == 'size':
        print(len(deque))
    elif command == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
    elif command == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])