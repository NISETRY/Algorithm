import heapq, sys
from heapq import heappop, heappush
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    num = int(input())
    lst.append(num)
answer = 0
tmp = [0]
    
while lst:
    
    heappush(tmp, heappop(lst))
    if len(tmp) == 2:
        answer += sum(tmp)
        heappush(tmp, answer)
print(tmp[0])