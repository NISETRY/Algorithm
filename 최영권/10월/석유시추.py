from collections import deque

def solution(land):
    R, C = len(land), len(land[0])
    visited = [[0]*C for _ in range(R)]

    # 각 열을 뚫었을 때 얻는 석유량 누적
    col_gain = [0]*C

    # 4방향
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    for sr in range(R):
        for sc in range(C):
            if land[sr][sc] == 1 and not visited[sr][sc]:
                # 새로운 석유 덩어리 BFS
                q = deque([(sr, sc)])
                visited[sr][sc] = 1
                gallon = 1           # 석유 양 누적시킬 변수
                touched_cols = {sc}  # 이 덩어리가 닿아있는 열들의 set

                while q:
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < R and 0 <= nc < C and land[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = 1
                            q.append((nr, nc))
                            gallon += 1
                            touched_cols.add(nc)

                # 이 덩어리 크기를, 닿아있는 모든 열에 누적
                for col in touched_cols:
                    col_gain[col] += gallon

    return max(col_gain)