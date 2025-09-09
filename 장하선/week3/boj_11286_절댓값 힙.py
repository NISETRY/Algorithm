import sys, heapq
input=sys.stdin.readline
n=int(input())
heap=[]
for i in range(n):
    k=int(input())
    if k!=0:
        heapq.heappush(heap, (abs(k),k))
    elif heap:
        tmp=heapq.heappop(heap)[1]
        print(tmp)
    else:
        print(0)