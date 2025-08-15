import sys
input=sys.stdin.readline
from collections import deque
n=int(input())
deck=deque()
for _ in range(n):
    k=input().split()
    if k[0]=='push_front':
        deck.appendleft(k[1])
    elif k[0]=='push_back':
        deck.append(k[1])
    elif k[0]=='pop_front':
        print(deck.popleft() if deck else -1)
    elif k[0]=='pop_back':
        print(deck.pop() if deck else -1)
    elif k[0]=='size':
        print(len(deck))
    elif k[0]=='empty':
        print(1 if not deck else 0)
    elif k[0]=='back':
        print(deck[-1] if deck else -1)
    else:
        print(deck[0] if deck else -1)