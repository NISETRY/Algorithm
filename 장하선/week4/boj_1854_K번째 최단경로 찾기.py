# 최단경로가 아닌 'k번째' 최단이니까 일단은 pq를 사용

from heapq import heappop, heappush
n,m,k=map(int,input().split())


