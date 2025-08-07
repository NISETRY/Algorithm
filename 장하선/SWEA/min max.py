T=int(input())
for t in range(1,T+1): 
    input()
    min_num=999999999
    max_num=-999999999
    z=list(map(int, input().split()))
    for x in z:
        if x>max_num:
            max_num=x
        if x<min_num:
            min_num=x
    print(f'#{t} {max_num-min_num}')