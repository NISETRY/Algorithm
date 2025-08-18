def switch(lst, idx):
    for i in range(idx,n):
        lst[i]=(lst[i]+1)%2
    return lst

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    cur_switch=list(map(int,input().split()))
    aim_switch=list(map(int,input().split()))
    cnt=0
    for i in range(n):
        if cur_switch[i]!=aim_switch[i]:
            cur_switch=switch(cur_switch, i)
            cnt+=1
    print(f'#{tc} {cnt}')