T=int(input())
for tc in range(1,T+1):
    n=int(input())
    omok=[input() for _ in range(n)]
    rev_omok=['' for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rev_omok[i]+=omok[j][i]
    flag=False
    # 가로오목
    for i in range(n):
        if 'ooooo' in omok[i]:
            flag=True
            break
    # 세로오목
    if not flag:
        for i in range(n):
            if 'ooooo' in rev_omok[i]:
                flag=True
                break
    # 대각오목
    if not flag:
        for x in range(n-4):
            for y in range(n-4):
                cnt=0
                for i in range(5):
                    if omok[x+i][y+i]=='o':
                        cnt+=1
                        if cnt==5:
                            flag=True
                            break
                    else:
                        cnt=0
                if flag:
                    break
            if flag:
                break
    if not flag:
        for x in range(n-4):
            for y in range(n-4):
                cnt=0
                for i in range(5):
                    if omok[n-1-x-i][y+i]=='o':
                        cnt+=1
                        if cnt==5:
                            flag=True
                            break
                    else:
                        cnt=0
                if flag:
                    break
            if flag:
                break
    if flag:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
