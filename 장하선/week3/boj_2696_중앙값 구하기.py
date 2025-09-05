import sys, heapq
input=sys.stdin.readline
T=int(input())
for tc in range(T):
    n=int(input())
    print(n//2+1)
    i=0
    max_heap=[]
    min_heap=[]
    for j in range(n//10+1):
        for x in map(int, input().split()):
            