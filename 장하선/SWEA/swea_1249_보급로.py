# import sys
# sys.stdin=open('input.txt')

from heapq import heappop,heappush
# 상하좌우
dr=[-1,1,0,0]
dc=[0,0,-1,1]


T=int(input())
for tc in range(1,T+1):
    n=int(input())
    road=[list(map(int,input().strip())) for i in range(n)]

    print(f'{tc} {ans}')