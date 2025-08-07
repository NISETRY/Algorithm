N = int(input())
for z in range(N):
      
    doku = [[-1 for _ in range(9)] for _ in range(9)]
  
    for r in range(9):
        inp = list(map(int, input().split()))
        for c in range(9):
            doku[r][c] = inp[c]
    # 입력
  
    for i in range(9):
        ans = 1
        temp = []
        temp2 = []
          
        for j in range(9):
            temp.append(doku[i][j])
            temp2.append(doku[j][i])
  
        if len(set(temp2)) != len(temp2) or len(set(temp)) != len(temp):
             ans = 0
             break
          
        for x in range(0,9,3):
            for y in range(0,9,3):
                temp3 = []
                for a in range(3):
                    for b in range(3):
                        temp3.append(doku[a+x][b+y])
                if len(temp3) != len(set(temp3)):
                    ans = 0
                      
                  
    if ans == 0:
        print(f'#{z+1} {0}')
    else:
        print(f'#{z+1} {1}')