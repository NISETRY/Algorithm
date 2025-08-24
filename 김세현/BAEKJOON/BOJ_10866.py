import sys

input = sys.stdin.readline

n = int(input())

sent = [input() for _ in range(n)]

deque = []

for c in sent:
    if 'push_front' in c.split()[0]:
        deque.insert(0, c.split()[1])
    elif 'push_back' in c.split()[0]:
        deque.append(c.split()[1])
    elif 'pop_front' in c:
        print(deque.pop(0)) if deque else print(-1)
    elif 'pop_back' in c:
        print(deque.pop(-1)) if deque else print(-1)
    elif 'size' in c:
        print(len(deque))
    elif 'empty' in c:
        print(0) if deque else print(1)
    elif 'front' in c:
        print(deque[0]) if deque else print(-1)
    elif 'back' in c:
        print(deque[-1]) if deque else print(-1)