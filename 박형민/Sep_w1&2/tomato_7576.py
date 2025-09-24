'''
토마토가 상하좌우로만 간다 -> 벡터사용
토마토 상태는 1: 익음 0: 안익음: -1: 비어 있음 세개다
시작점이 정해져 있고 돌아오지 않으므로 선형탐색이다
visited 사용 -> 선형탐색 이니까 안써도 되지 않을까?
BFS 가 맞는 듯
DFS??
'''
from pprint import pprint
from collections import deque

M, N = map(int, input().split())        # M = c, N = r
arr = [ list(map(int, input().split())) for _ in range(N)]

# print(arr)

dr = [1, -1, 0, 0]      # 上下左右
dc = [0, 0, -1, 1]

# print(arr[3][5])        # 1

cnt = 0
q = deque([])

def bfs():
    global cnt
    while q:
        r, c = q.popleft()

        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]

            if 0 <= new_r <= N-1 and 0 <= new_c <= M-1:
                if arr[new_r][new_c] == 0:
                    arr[new_r][new_c] = arr[r][c] + 1
                    q.append([new_r, new_c])



for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i, j])

bfs()
ans = 0
# pprint(arr)
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))

print(ans - 1)
