import sys, heapq
input=sys.stdin.readline
n=int(input())

heap=[]
for _ in range(n):
    for x in map(int, input().split()):
        if len(heap) < n:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)

print(heap[0])