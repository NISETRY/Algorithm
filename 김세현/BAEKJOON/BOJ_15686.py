N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 좌표 값 1: 그냥 집
house = [] # 그냥 집 x, y 좌표
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])

# 좌표 값 2: 치킨 집
chi = [] # 치킨 집 x, y 좌표
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chi.append([i, j])

# 거리 계산 (2차원 리스트로)
length = []
for c in chi:
    row = []
    for h in house:
        cha = abs(h[0] - c[0]) + abs(h[1] - c[1])
        row.append(cha)
    length.append(row)

picked = []
min_total = 1e9
a = []

def comb(count, idx):
    global min_total 

    if 1 <= count <= M:
        hab = 0
        for j in range(len(house)):
            min_l = 1e9
            for i in range(len(picked)):
                min_l = min(picked[i][j], min_l)
            hab += min_l
        a.append(hab)

    if count == M:
        return
    
    for i in range(idx, len(chi)):
        picked.append(length[i])
        comb(count + 1, i + 1)
        picked.pop()

comb(0,0)
print(min(a))

  