t = int(input())

def enq(n):
    global last
    
    min_heap[last] = n
    p = last // 2
    now = last

    while p > 0 and min_heap[p] > min_heap[now]:
        min_heap[p], min_heap[now] = min_heap[now], min_heap[p]
        now = p
        p = p // 2

    last += 1
        
    
    

for tc in range(t):
    n = int(input())
    graph = list(map(int, input().split()))
    min_heap = [0]*(n+1)
    last = 1

    for i in graph:
        enq(i)

    ans = 0
    last = len(min_heap)-1
    p = 99
    while p>0:
        p = last//2
        ans += min_heap[p]
        last = p

    print(f'#{tc+1} {ans}')
    