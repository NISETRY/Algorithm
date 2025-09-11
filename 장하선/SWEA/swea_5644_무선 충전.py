T=int(input())
#x상우하좌
dr=[0,-1,0,1,0]
dc=[0,0,1,0,-1]

def charge(x1,y1,x2,y2):
    charge_a, charge_b=[],[]
    for i in range(n):
        cx,cy,dis,p=ap[i]
        if abs(x1-cx)+abs(y1-cy)<=dis:
            charge_a.append(i)
        if abs(x2-cx)+abs(y2-cy)<=dis:
            charge_b.append(i)
    charge_a.append(-1)
    charge_b.append(-1)
    realmax=-1
    charge_amount=(0,0)
    for a in charge_a:
        for b in charge_b:
            if a==-1 and b==-1:
                max_a,max_b=0,0
            elif a==b and a!=-1:
                tmp=ap[a][3]
                max_a,max_b=tmp//2,tmp//2
            else:
                max_a=ap[a][3] if a!=-1 else 0
                max_b=ap[b][3] if b!=-1 else 0
            tot=max_a+max_b
            if tot > realmax:
                realmax=tot
                charge_amount=(max_a,max_b)
    return charge_amount

for tc in range(1,T+1):
    t,n=map(int, input().split())
    dir_a=[0]+list(map(int, input().split()))
    dir_b=[0]+list(map(int, input().split()))
    res_a, res_b=0,0
    xa,ya,xb,yb=0,0,9,9
    ap=[[] for _ in range(n)]
    for i in range(n):
        x,y,ditance,power=map(int, input().split())
        ap[i]=(y-1,x-1,ditance,power)
    # print(ap)
    for i in range(t+1):
        nxa,nya,nxb,nyb=xa+dr[dir_a[i]],ya+dc[dir_a[i]],xb+dr[dir_b[i]],yb+dc[dir_b[i]]
        tmp1, tmp2=charge(nxa,nya,nxb,nyb)
        res_a+=tmp1
        res_b+=tmp2
        print(i, res_a,res_b)
        xa,ya,xb,yb=nxa,nya,nxb,nyb
    print(f'#{tc} {res_a+res_b}')