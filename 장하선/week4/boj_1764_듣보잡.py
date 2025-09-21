import sys
input=sys.stdin.readline

n,m=map(int,input().split())
hear=set()
seen=set()
hear={input().rstrip() for _ in range(n)}
seen={input().rstrip() for _ in range(m)}
dutbo=sorted(hear&seen)
print(len(dutbo))
print("\n".join(dutbo))