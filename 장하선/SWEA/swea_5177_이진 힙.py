T=int(input())
def enq(node):
    global last
    last+=1
    heap[last]=node
    c=last
    p=c//2
    while p>0 and heap[p]>heap[c]:
        heap[p],heap[c]=heap[c],heap[p]
        c,p=p,c//2

for tc in range(1,T+1):
    last=0
    n=int(input())
    info=list(map(int,input().split()))
    heap=[0]*(n+1)
    for x in info:
        enq(x)
    res=0
    while n>0:
        n//=2
        res+=heap[n]
    print(f'#{tc} {res}')