import sys, heapq
input=sys.stdin.readline
n=int(input())
hque=[]
for i in range(n):
    k=int(input())
    if k>0:
        heapq.heappush(hque, (-k, k))
    elif hque:
        k=heapq.heappop(hque)[1]
        print(k)
    else:
        print(0)
