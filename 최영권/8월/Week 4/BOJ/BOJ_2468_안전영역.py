# N*N 2차원 배열에서
# 물 높이 : 잠기기 시작하는 높이의 최소값부터 모든 영역이 다잠기는 높이의 최대값까지 반복
# BFS를 위한 덱 생성
from collections import deque

N = int(input())

min_height = 101
max_height = 0
graph = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in temp:
        max_height = max(max_height, j)
        min_height = min(min_height, j)
    graph.append(temp)

d = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs():
    global count
    while q:
        sr, sc = q.popleft()
        for dr, dc in d:
            nr = sr + dr
            nc = sc + dc
            if 0<=nr<N and 0<=nc<N and graph[nr][nc] > height and visited[nr][nc] ==0:
                q.append((nr, nc))
                visited[nr][nc] = 1
    count += 1
    return count


# 물 높이보다 영역의 높이가 더 높은 곳을 만나면 BFS시작 -> 탐색
max_count = 0
if min_height == max_height:
    max_count = 1
else:
        
    for height in range(min_height, max_height+1):
        q = deque([])
        visited = [[0] * N for _ in range(N)]
        count = 0 
        for r in range(N):
            for c in range(N):
                if graph[r][c] > height and visited[r][c] == 0:
                    q.append((r, c))
                    visited[r][c] = 1
                    bfs()
    # 현재 물 높이에서 영역의 갯수와 최대 영역의 갯수를 비교
        max_count = max(max_count, count)


print(max_count)





