def comb(count, idx):
    if count == m:
        pick.append(temp[:])
        return
    
    for i in range(1, n*n+1):
        r, c = for_comb[i-1]
        if i>idx:
            temp.append([r,c])
            comb(count+1, i)
            temp.pop()

t = int(input())
for tc in range(t):
    n, m, c = map(int,input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    for_comb = [(p,q) for p in range(n) for q in range(n)]
    
    temp = []
    pick = []
    comb(0,0)
    
    for i in pick:
        print(i)
        
# 모든 경우의 수에 대해서 벌꿀제곱합을 구하고, sort한 다음에 앞에 두개 더하면 될 듯..?
# 근데, 벌꿀제곱합을 구할 때 조합을 한 번 더 써야하나..?