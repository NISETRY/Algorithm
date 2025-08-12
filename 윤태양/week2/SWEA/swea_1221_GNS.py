t = int(input())
 
for tc in range(t):
    input()
    l = list(input().split())
    cnt = [0]*10
    alp = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]
 
    for i in range(len(l)):
        if l[i] == 'ZRO':
            cnt[0] += 1
        elif l[i] == 'ONE':
            cnt[1] += 1
        elif l[i] == 'TWO':
            cnt[2] += 1
        elif l[i] == 'THR':
            cnt[3] += 1
        elif l[i] == 'FOR':
            cnt[4] += 1
        elif l[i] == 'FIV':
            cnt[5] += 1
        elif l[i] == 'SIX':
            cnt[6] += 1
        elif l[i] == 'SVN':
            cnt[7] += 1
        elif l[i] == 'EGT':
            cnt[8] += 1
        elif l[i] == 'NIN':
            cnt[9] += 1
             
    print(f'#{tc+1}')
    for i in range(10):
        print(cnt[i]*alp[i], end='')