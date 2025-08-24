
# 백준 7576번 토마토

from collections import deque

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 익은 토마토 1, 안익은 토마토 0, 토마토없음 -1
# 최종 결과는 1과 -1로만 이루어져 있어야 함

# 모두 익을 때까지 최소 날짜 출력 -> 최소 날짜니까 BFS(최단경로)

# def BFS()

# 익은 토마토 먼저 찾기 (1 찾기)
# 상,하,좌,우로 탐색하면서 0이면 1로 변경하기
# -1 이면 이동 못함. 
# 1로 변경하면 날짜를 셀건데, 동시에 변경 가능인데 언제 해야하지? 

# 근데 1이 여러개면 동시에 영향을 줘서 한번에 변경 가능한데, 이걸 어케 해야하지
# 일단 1이 있는 곳을 다 찾아. 
# 그리고 동시에 다 도는거지. 가능한가? - 근데 사실 이게 되는게 BFS 아닌가?

day = 0
q = deque()


# 익은 토마토 있는 곳 찾기
for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            
            q.append((r,c)) # 익은 토마토 위치 찾아서 저장하기
        
visited = [[0]*M for _ in range(N)]


# BFS
while q:
    # 큐에서 현재 가야할 곳으로 선정
    curr_r, curr_c = q.popleft()

    # 4방향 탐색
    for k in range(4):
        nr = curr_r + dr[k]
        nc = curr_c + dc[k]

        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0 and visited[nr][nc] == 0 :
            graph[nr][nc] = 1      # 방문 처리
            q.append((nr, nc))    # 큐에 추가
            visited[nr][nc] = visited[curr_r][curr_c] + 1

# print(graph)

answer_day = 0
flag = False
for r in range(N):
    for c in range(M):
        if graph[r][c] == 0:
            answer_day = -1
            flag = True
            break
    
        answer_day = max(map(max,visited))

    if flag:
        break

print(answer_day)
