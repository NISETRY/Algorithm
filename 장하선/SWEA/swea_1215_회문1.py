def palin():
    cnt=0
    for i in range(8):
        for j in range(9-n):
            for x in range(n//2):
                if letters[i][j+x]!=letters[i][j+n-x-1]:
                    break
            else:
                cnt+=1  
    return cnt              
for tc in range(1,11):
    n=int(input())
    letters=[[] for _ in range(8)]
    for i in range(8):
        letters[i]=list(input())
    cnt1=palin()
    for i in range(8):
        for j in range(i):
            letters[i][j], letters[j][i] = letters[j][i], letters[i][j]
    cnt2=palin()
    res=cnt1+cnt2
    print(f'#{tc} {res}')