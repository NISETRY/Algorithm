from itertools import combinations
from collections import deque
import sys
sys.stdin = open("input.txt")

# BFS 의 시간 복잡도는 K(치킨집 수) Comb M * N^2

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():

    q = deque()
    # 갈 칸이 현재 칸(스텝 수)보다 이하일 때 안가면 됨 => 이렇게 되면 애초에 처음부터 시작하지를 않음
    # 따라서 (N-1) * 2 까지 나올 수 있기에 이보다 1 큰 (N-1) * 2 + 1 을 넣어서 배열을 만듦
    visited = [ [(N-1) * 2 + 1] * N for _ in range(N) ]

    for store_idx in store_idx_set:
        r, c = store_rcs[store_idx]
        visited[r][c] = 0
        q.append((r, c))

    while q:
        r, c = q.popleft()

        for dir in range(4):
            nr = r+dr[dir]
            nc = c+dc[dir]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if visited[nr][nc] <= visited[r][c] + 1:
                continue

            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))

    distance = 0
    for r, c in home_rcs:
        distance += visited[r][c]

    return distance



N, M = map(int, input().split())

# 입력 정보 입력과 동시에 각 집의 정보도 받아옴
graph = [[0] * N for _ in range(N)]

home_rcs = []
store_rcs = []
answer = float('inf')

for r in range(N):
    row = list(map(int, input().split()))

    for c in range(N):
        graph[r][c] = row[c]

        if graph[r][c] == 1:
            home_rcs.append((r, c))
        elif graph[r][c] == 2:
            store_rcs.append((r, c))


for store_idx_set in combinations(range(len(store_rcs)), M):


    answer = min(answer, distance)