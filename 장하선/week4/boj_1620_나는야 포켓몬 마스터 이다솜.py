import sys
# sys.stdin=open('input.txt')
input=sys.stdin.readline

n,m=map(int,input().split())
poke=[input().rstrip() for _ in range(n)]
pokedict={name: i+1 for i, name in enumerate(poke)}
for i in range(m):
    ans=input().rstrip()
    if ans.isdigit():
        print(poke[int(ans)-1])
    else:
        print(pokedict[ans])