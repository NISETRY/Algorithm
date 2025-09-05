import sys, heapq
input=sys.stdin.readline
n=int(input())
heap=[]
for i in range(n):
    k=int(input())
    if k>0:
        heapq.heappush(heap, k)
    elif heap:
        tmp=heapq.heappop(heap)
        print(tmp)
    else:
        print(0)