# 순서 : 넣고, 녹고, 돌리고
from collections import deque
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    pizza=list(map(int,input().split()))
    cnt=n
    out=[]
    napoli=deque(pizza[:n])
    pizza_num=deque([i+1 for i in range(n)])
    pizza=pizza[n:]    
    while napoli:     
        c=napoli.popleft()
        idx=pizza_num.popleft()
        c//=2

        if c==0:
            out.append(idx)
            if pizza:
                cnt+=1
                napoli.append(pizza.pop(0))
                pizza_num.append(cnt)
        else:
            napoli.append(c)
            pizza_num.append(idx)

    # print(out)
    print(f'#{tc} {out[-1]}')
