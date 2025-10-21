import heapq
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
N = int(input())
lst = []
for i in range(N):
    order = int(input())
    if order == 0:
        if not lst:
            print(0)
        else:
            print(heappop(lst))
    
    else:
        heappush(lst, order)
