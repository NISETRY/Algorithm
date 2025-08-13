def comb(count, idx):
    if count == m:
        pick.append(temp[:])
        return
    
    for i in range(1, n*n+1):            # 벌꿀 고르는 조합 만들기
        r, c = for_comb[i-1]                    
        if i>idx:                        # count 조건 
            if temp:
                p, q = temp[-1]
                if r == p and q+1 == c:  # 연속 조건
                    temp.append([r,c])
                    comb(count+1, i)
                    temp.pop()
            else:                          
                temp.append([r,c])
                comb(count+1, i)
                temp.pop()

t = int(input())
for tc in range(t):
    n, m, c = map(int,input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    for_comb = [(p,q) for p in range(n) for q in range(n)] # 벌꿀 조합용 1차원 리스트
    
    temp = []
    pick = []
    comb(0,0)
    ans = []

    for i in pick:
        honey = []
        for j in range(len(i)):
            honey.append((graph[i[j][0]][i[j][1]],i[j][0]))

        honey.sort(reverse=True) # 벌꿀 소트 후 탐색
        for r in range(len(honey)):
            tp = []
            sq = 0
            
            for r2 in range(r, len(honey)):
                tp.append(honey[r2][0])
                if sum(tp) > c:
                    tp.pop()

            for i in range(len(tp)):
                sq += tp[i]**2
            ans.append([sq, honey[r2][1]])
    # print(ans)
    ans.sort()
    ans2 = []
    d = -1
    while len(ans2) != 2:
        a, b = ans.pop()
        if b != d:
            ans2.append(a)
            d = b

    print(f'#{tc+1} {sum(ans2)}')

                    

        
