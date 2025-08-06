n, m = map(int,input().split())
graph = [[0]*n for _ in range(n)]
idx_c = [[0,0]]
idx_h = []
num_c = 0

for q in range(n):                              # 인풋
    temp = list(map(int, input().split()))
    for p in range(n):
        graph[q][p] = temp[p]

        if temp[p] == 2:                        # 치킨집 위치 따로 저장
            num_c+=1
            idx_c.append([q,p])
        
        elif temp[p] == 1:                      # 집 위치 따로 저장
            idx_h.append([q,p])

combs = []
temp = []
def comb(count, idx):                           # 치킨집 조합
    if count == m:
        combs.append(temp[:])
        return
    
    else:
        for i in range(1, num_c+1):
            if i > idx:
                temp.append(i)
                comb(count+1, i)
                temp.pop()
comb(0,0)
min_d = 10000000000

for i in combs:                               #치킨집 조합 경우의 수
    dis = [10000]*len(idx_h)
    for j in range(m):                            
        c_x, c_y = idx_c[i[j]][0], idx_c[i[j]][1] # 경우의 수 -> 위치 변환
 
        for k in range(len(idx_h)):
            dis_ch = abs(c_x - idx_h[k][0]) + abs(c_y - idx_h[k][1]) # 집과 치킨집 거리 
            dis[k] = min(dis[k], dis_ch)  # 최소거리 
        
        # print(f'{k:} {dis}')
        min_d = min(sum(dis), min_d) 

print(min_d)
    