import sys
input=sys.stdin.readline
interpreter=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    
T=int(input())
for tc in range(1,T+1):
    input()
    planet_nums=list(input().split())
    sorted_nums=[]
    cnt=[0 for _ in range(10)]
    for i in range(10):
        cnt[i]=planet_nums.count(interpreter[i])
    for x in range(10):
        sorted_nums.extend([interpreter[x] * cnt[x]])
    print(f'#{tc}', end=' ')
    print(*sorted_nums)