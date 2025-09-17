import sys, heapq
input=sys.stdin.readline
def num_push(x):
    if len(max_heap)==len(min_heap):
        heapq.heappush(min_heap,x)
    else:
        heapq.heappush(max_heap, -x)

    if max_heap and -max_heap[0]>min_heap[0]:
        tmp_min=heapq.heappop(min_heap)
        tmp_max=heapq.heappop(max_heap)
        heapq.heappush(max_heap, -tmp_min)
        heapq.heappush(min_heap, -tmp_max)

def median_finder():
    return min_heap[0]    

T=int(input())
for tc in range(T):
    n=int(input())
    print(n//2+1)
    cnt=0
    max_heap=[]
    min_heap=[]
    nums=[]
    mids=[0 for _ in range(n//2+1)]
    for j in range(n//10+1):
        for x in map(int, input().split()):
            num_push(x)
            cnt+=1
            if cnt%2==1:
                mids[cnt//2]=median_finder()
    for i in range(0,cnt//2+1,10):
        print(*mids[i:i+10])