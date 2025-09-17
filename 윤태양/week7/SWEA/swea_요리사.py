def comb(count, idx):
    global min_gap

    if count == n//2:
        if temp[0] != 0:
            return
        
        not_pick = list(set([i for i in range(n)]) - set(temp))
        t1, t2 = 0, 0
        for i in temp:
            for j in temp:
                t1 += graph[i][j]

        for i in not_pick:
            for j in not_pick:
                t2 += graph[i][j]
                
        min_gap = min(min_gap, abs(t1-t2))
        return
    
    for i in range(n):
        if i>idx:
            temp.append(i)
            comb(count+1, i)
            temp.pop()
        

t = int(input())

for tc in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    temp = []
    min_gap = 99999999999999999999
    comb(0,-1)
    print(f'#{tc+1} {min_gap}')
    