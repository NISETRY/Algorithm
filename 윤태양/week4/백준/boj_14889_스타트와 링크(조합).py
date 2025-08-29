temp = []
picked = []

def comb(count, idx):            # 조합 생성
    if count == n/2:
        picked.append(temp[:])
        return
    
    for i in range(1, n+1):
        if i > idx:
            temp.append(i)
            comb(count+1, i)
            t = temp.pop()
            if t == 1:           # 만약에 1이 뽑히면 return 
                return

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

comb(0,0)
min_gap = 101
for pick in picked:
    not_pick = list(set([_ for _ in range(1,n+1)]) - set(pick))
    pick_sum, not_pick_sum = 0, 0

    for i in pick:
        for j in pick:
            pick_sum += graph[i-1][j-1]

    for i in not_pick:
        for j in not_pick:
            not_pick_sum += graph[i-1][j-1]

    gap = abs(pick_sum-not_pick_sum)
    min_gap = min(gap, min_gap)  

print(min_gap)



