from heapq import heappop, heappush

V,E=map(int,input().split())
k=int(input())
roots=[]
for i in range(E):
    u,v,w=map(int,input().split())
    heappush(roots, (w,u,v))
