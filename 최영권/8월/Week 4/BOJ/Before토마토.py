# # 백준 7576번 토마토 pair coding

# from collections import deque

# M, N = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(N)]

# # 상, 하, 좌, 우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# # 익은 토마토 1, 안익은 토마토 0, 토마토없음 -1
# # 최종 결과는 1과 -1로만 이루어져 있어야 함

# # 모두 익을 때까지 최소 날짜 출력 -> 최소 날짜니까 BFS(최단경로)

# # def BFS()

# # 익은 토마토 먼저 찾기 (1 찾기)
# # 상,하,좌,우로 탐색하면서 0이면 1로 변경하기
# # -1 이면 이동 못함. 
# # 1로 변경하면 날짜를 셀건데, 동시에 변경 가능인데 언제 해야하지? 

# # 근데 1이 여러개면 동시에 영향을 줘서 한번에 변경 가능한데, 이걸 어케 해야하지
# # 일단 1이 있는 곳을 다 찾아. 
# # 그리고 동시에 다 도는거지. 가능한가? - 근데 사실 이게 되는게 BFS 아닌가?

# day = 0
# q = deque()


# # 익은 토마토 있는 곳 찾기
# for r in range(N):
#     for c in range(M):
#         if graph[r][c] == 1:
            
#             q.append((r,c)) # 익은 토마토 위치 찾아서 저장하기
        
# visited = [[0]*M for _ in range(N)]


# # BFS
# while q:
#     # 큐에서 현재 가야할 곳으로 선정
#     curr_r, curr_c = q.popleft()

#     # 4방향 탐색
#     for k in range(4):
#         nr = curr_r + dr[k]
#         nc = curr_c + dc[k]

#         if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0 and visited[nr][nc] == 0 :
#             graph[nr][nc] = 1      # 방문 처리
#             q.append((nr, nc))    # 큐에 추가
#             visited[nr][nc] = visited[curr_r][curr_c] + 1

# # print(graph)

# answer_day = 0
# flag = False
# for r in range(N):
#     for c in range(M):
#         if graph[r][c] == 0:
#             answer_day = -1
#             flag = True
#             break
    
#         answer_day = max(map(max,visited))

#     if flag:
#         break

# print(answer_day)

## 코드 by 임서영
# from collections import deque

# def tomato(t, sx, sy):
#     global zero_count

#     q = deque()
#     for i in range(len(sx)):
#         q.append((sx[i], sy[i]))

#     step = -1
#     while q:
#         for _ in range(len(q)):
#             x, y = q.popleft()
#             # 네 방향 탐색해서 다음 탐색지점 선정
#             for dx, dy in dir:
#                 nx = dx + x
#                 ny = dy + y
#                 if 0 <= nx < N and 0 <= ny < M:
#                     if t[nx][ny] == 0:
#                         zero_count -= 1
#                         t[nx][ny] = 1
#                         q.append((nx, ny))
#         step += 1
#     print(t)
#     if zero_count != 0:
#         return -1
#     else:
#         return step


# M, N = map(int, input().split())
# dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# tomatoes= []

# sx = []
# sy = []
# zero_count = 0

# for i in range(N):
#     temp = list(map(int, input().split()))
#     for j in range(M):
#         if temp[j] == 1:
#             sx.append(i)
#             sy.append(j)
#         elif temp[j] == 0:
#             zero_count += 1
#     tomatoes.append(temp)

# result = tomato(tomatoes, sx, sy)
# print(result)


## 제출 토마토 BY 최영권
# from collections import deque
# import pprint
# M, N = map(int, input().split())
# tomato = []
# que = deque()
# for i in range(N):
#     temp = list(map(int, input().split()))
#     for j in range(M):
#         if temp[j] == 1:
#             que.append((i,j))
#     tomato.append(temp)

# d = [(1,0), (-1,0), (0,1), (0,-1)]


# day = -1
# def raise_tomatoes(t, que):
#     global day
#     q = deque()
#     for si, sj in que:
#         q.append((si, sj))
    
#     while q:
        
#         for _ in range(len(q)):
#             tr, tc = q.popleft()
#             for dr, dc in d:
#                 nr = tr + dr
#                 nc = tc + dc
#                 if 0<=nr<N and 0<=nc<M and t[nr][nc] == 0:
#                     t[nr][nc] = 1
#                     q.append((nr,nc))
                
#         day += 1
#     # pprint.pprint(t)
#     zero_count = 0
#     for i in t:
#         for j in i:
#             if j == 0:
#                 zero_count += 1
#                 break
#     if zero_count != 0:
#         return -1
#     else:
#         return day
# answer = raise_tomatoes(tomato, que)
# print(answer)

 # 백준 7576번 토마토
## 강사님 풀이 코드
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
answer_day = max(map(max,visited))

for r in range(N):
    for c in range(M):
        if graph[r][c] == 0:
            answer_day = -1
            flag = True
            break
    

    if flag:
        break


print(answer_day)