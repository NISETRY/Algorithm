from collections import deque

import sys
T = int(sys.stdin.readline())
lst = deque()
for i in range(T):
    command = sys.stdin.readline().strip()
    if command.startswith('push'):
        word, num = command.split()
        lst.append(num)
    elif command == "top":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    elif command == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif command == 'size':
        print(len(lst))
    elif command == 'pop':
        
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())