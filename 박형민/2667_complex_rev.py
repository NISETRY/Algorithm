# 배열 탐색하다가 1이 있으면 dfs 시작
# dfs 한 번 돌때마다 cnt += 1
# visitied 처리 해주어 배열 순회 중 다시 안돌게
# 델타로 사방탐색

from collections import deque
N = int(input())
arr = [ list(map(int, input())) for _ in range(N) ]
visitied = [ [0] * N for _ in range(N) ]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
complex = deque()

def dfs(r, c):
    global cnt
    while complex:
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr <= N-1 and 0 <= nc <= N-1:
                if arr[nr][nc] == 1 and visitied[nr][nc] == 0:
                    complex.append((r, c))
                    cnt += 1
                    dfs(nr, nc)
                    complex.pop()

ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visitied[i][j] == 0:
            cnt = 1
            dfs(i, j)
            ans.append(cnt)
            
print(len(ans))
# print(ans)