import sys
sys.stdin=open('i.txt')

def find(x):
    if x==parent[x]: return x
    parent[x]=find(parent[x])
    return parent[x]
 
def union(a,b):
    a,b=find(a),find(b)
    if a<b: parent[b]=a
    else: parent[a]=b
 
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    couple=[[]for _ in range(m)]
    pick=list(map(int,input().split()))
    parent=[i for i in range(n+1)]
    for i in range(m): couple[i]=(pick[i*2],pick[i*2+1])
    for i in range(m):
        a,b=couple[i]
        union(a,b)
    roots=set(find(i) for i in range(1,n+1))
    print(f'#{tc} {len(roots)}')