T=int(input())
for tc in range(1,T+1):
    P,Pa,Pb=map(int,input().split())
    cnt_a,cnt_b=0,0
    def binary(search, cnt):
        l,r=1,P
        while l<=r:
            mid=int((l+r)/2)
            cnt+=1
            if mid==search:
                return cnt
            elif mid>search:
                r=mid
            else:
                l=mid
    cnt_a=binary(Pa,0)
    cnt_b=binary(Pb,0)
    if cnt_a < cnt_b:
        winner = 'A'
    elif cnt_b < cnt_a:
        winner = 'B'
    else:
        winner = 0
    print(cnt_a,cnt_b)
    print(f'#{tc} {winner}')