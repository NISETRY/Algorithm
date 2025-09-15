import sys
input=sys.stdin.readline

n,m=map(int, input().split())
setting=[i for i in range(n+1)]

def find(x):
    while setting[x]!=x:
        setting[x]=setting[setting[x]]
        x=setting[x]
    return setting[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        setting[b]=a
    else:
        setting[a]=b

for i in range(m):
    op,a,b=map(int,input().split())
    if op==0:
        union(a,b)
    else:
        print('yes' if find(a)==find(b) else 'no')