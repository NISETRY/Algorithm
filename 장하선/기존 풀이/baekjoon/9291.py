T=int(input())
for t in range(1,1+T):
    sud=[]
#스도쿠 생성
    for _ in range(9):
        row=list(map(int, input().split()))
        sud.append(row)
    correct=True
#가로검사
    for i in range(9):
        check=[0]*10
        for j in range(9):
            if check[sud[i][j]]==0:
                check[sud[i][j]]=1
            else:
                correct=False
                break
#세로검사
    if correct:
        for i in range(9):
            check=[0]*10
            for j in range(9):
                if check[sud[j][i]]==0:
                    check[sud[j][i]]=1
                else:
                    correct=False
                    break
#상자검사
    if correct:
        for x in range(0,9,3):
            for y in range(0,9,3):
                check=[0]*10
                for i in range(x,x+3):
                    for j in range(y,y+3):
                        if check[sud[i][j]]==0:
                            check[sud[i][j]]=1
                        else:
                            correct=False
                            break
#출력        
    if correct:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
#엔터처리
    if t<T:
        input()