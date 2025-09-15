from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

# 집, 치킨집 좌표 수집
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

answer = 1e9

# DFS로 집마다 최소 치킨거리 구하기
def dfs(h_idx, comb, total_dist):
    global answer
    
    # 모든 집 탐색 완료 → 도시 치킨 거리 갱신
    if h_idx == len(houses):
        answer = min(answer, total_dist)
        return
    
    hr, hc = houses[h_idx]
    min_dist = 1e9
    # 현재 조합의 치킨집 중 가장 가까운 거리 찾기
    for cr, cc in comb:
        dist = abs(hr - cr) + abs(hc - cc)
        min_dist = min(min_dist, dist)
    
    dfs(h_idx + 1, comb, total_dist + min_dist)

# 치킨집 M개 선택 조합 생성
for comb in combinations(chickens, M):
    dfs(0, comb, 0)

print(answer)
