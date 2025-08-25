t = int(input())

temp = []
combo = []
def comb(count, idx):
    combo.append(temp[:])
    if count == d:
        return
    
    for i in range(1, d+1):
        if i>idx:
            temp.append(i-1)
            comb(count+1, i)
            temp.pop()
    
permu = [] 

for tc in range(t):
    d,w,k = map(int, input().split()) # row,col,k
    graph = [list(map(int, input().split())) for _ in range(d)]

    comb(0,0)
    pick = sorted(combo, key=len)

    for i in pick:
        for r in range(d):
            for c in range(w):
                if r in i:
                    graph[r][c] = 1
        seri = []
        for p in range(w):
            for q in range(d):
                if not seri and graph[p][q] == 0:
                    seri.append(0,1)
                    continue

                if not seri and graph[p][q] == 1:
                    seri.append(1,1)
                    continue


# not_pick도 처리해야하고...
# 검사도 추가해야하고...
# 시간도 챙겨야함