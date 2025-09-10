# # 얕은 복사/깊은 복사 차이
# # 1. 바뀌는 지 안바뀌는 지, 주소 참조
# a = [1, 2, 3]
# b = a # 얕은 복사

# a[0] = 100
# print(b) # [100, 2, 3]

# # 벽돌 깨기에서 얕은 복사가 문제되는 이유
# # 슬라이싱은 1차원일 때는 깊은 복사가 되지만 2차원이면 얕은 복사

# DFS: 구슬을 어디에 떨굴지 순서를 정함 (중복순열)
# BFS: 연쇄 폭파를 기록하기 위한 용도

# 1. 해당 count번째에서 구슬을 떨어뜨릴 행(+열)을 고르기


# 2. 연쇄 폭발 영역을 탐색 > BFS


# 3. 폭발 & 떨어뜨리기
from collections import deque
 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
 
def crash(count, remain, graph):
    global answer
 
    if not remain or count == N:
        answer = min(answer, remain)
        return
     
    # 1. 해당 count 번째에서 구슬을 떨어뜨릴 행 고르기
    for i in range(W):
        next_remain = remain
         
        # * 해당 행이 비어있으면 스킵
        if not graph[i]:
            continue
 
        r = i
        c = len(graph[r])-1
     
        # 2. 연쇄 폭발 영역 탐색
        q = deque()
        visited = [[0]*H for _ in range(W)]
 
        # 폭발 시작점 초기화
        next_remain -= 1
        visited[r][c] = 1
        q.append((r, c))
 
        while q:
            r, c = q.popleft()
             
            if graph[r][c] <= 1:
                continue
             
            for dir in range(4):
                for step in range(1, graph[r][c]):
                     
                    nr = r+dr[dir]*step
                    nc = c+dc[dir]*step
 
                    if nr < 0 or nr >= W or nc < 0 or nc >= H:
                        continue
                    if visited[nr][nc] == 1:
                        continue
                    if len(graph[nr])-1 < nc:
                        continue
 
                    next_remain -= 1
                    visited[nr][nc] = 1
                    q.append((nr, nc))
 
        # 3. 폭파 & 떨어뜨리기
        copy_graph = []
        for r in range(W):
            row = []
            for c in range(len(graph[r])):
                if visited[r][c]:
                    continue
                row.append(graph[r][c])
            copy_graph.append(row)
 
        crash(count+1, next_remain, copy_graph)
 
T = int(input())
 
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
 
    input_graph = [list(map(int, input().split())) for _ in range(H)]
    graph = []
    answer = 0
 
    # 행렬 90도 회전 & 벽돌 수 기록
    for i in range(W):
        row = []
        for j in range(H):
            if input_graph[H-1-j][i] == 0:
                answer += j            
                break
            row.append(input_graph[H-1-j][i])
        else:
            answer += H
        graph.append(row)
 
    crash(0, answer, graph)
 
    print(f'#{tc} {answer}')