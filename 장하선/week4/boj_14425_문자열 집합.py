import sys
# sys.stdin=open('input.txt')
input=sys.stdin.readline

n,m=map(int,input().split())
letters=[input().rstrip() for _ in range(n)]
res=0
for i in range(m):
    if input().rstrip() in letters:
        res+=1
print(res)