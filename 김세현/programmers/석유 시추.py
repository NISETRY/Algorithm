from collections import deque

n, m = map(int, input().split()) # 세로 길이 n, 가로 길이 m

# 0 = 깨끗한 땅, 1 = 석유가 있는 땅
grid = [list(map(int, input().split())) for _ in range(n)]

# 시추관을 뽑을 수 있는 경우의 수는 m개
# 덩어리 개수 확인해서 1 대신 덩어리 값으로 바꾸기

visited = [[0]*m for _ in range(n)]
dirs = [(-1,0), (0,-1), (1,0), (0,1)]
# 덩어리 번호
cnt = 0
# 각 덩어리의 크기 저장
cnt_size = [0]

# BFS: 석유 덩어리 찾기
# 연결된 1들을 하나의 덩어리로 묶고, grid의 1을 덩어리 번호(cnt)로 치환, 각 덩어리의 크기(size) 기록
for r in range(n):
    for c in range(m):
        # 석유(1)인 곳, 아직 방문 안한 곳
        if grid[r][c] == 1 and visited[r][c] == 0:
            cnt += 1
            q = deque([(r,c)])
            visited[r][c] = 1
            grid[r][c] = cnt
            size = 1 # 덩어리 크기

            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < m:
                        # 아직 방문 안하고 석유(1)인 곳
                        if visited[nx][ny] == 0 and grid[nx][ny] == 1:
                            visited[nx][ny] = 1
                            grid[nx][ny] = cnt # 같은 덩어리 번호로 통일
                            size += 1
                            q.append((nx, ny))
        cnt_size.append(size) # 덩어리별 크기 저장

# 시추관 꽂았을 때 얻을 수 있는 석유량 계산
# 각 열이 닿는 서로 다른 덩어리 id 확인 (set로 중복 확인)
# 해당 덩어리들의 크기 합산
answer = 0
for col in range(m):
    seen = set()
    total = 0
    for row in range(n):
        bar = grid[row][col]
        if bar != 0:
            # 아직 한번도 더하지 않은 덩어리인지 확인
            if bar not in seen:
                # 더한 덩어리임을 표시
                seen.add(bar)
                # 덩어리 크기만큼 total에 더하기
                total += cnt_size[bar]

    answer = max(answer, total)

print(answer)


# 프로그래머스용 코드
# from collections import deque

# def solution(land):
#     n, m = len(land), len(land[0])

#     grid = [row[:] for row in land]  # 원본 유지용 복사
#     visited = [[0]*m for _ in range(n)]
#     dirs = [(-1,0), (0,-1), (1,0), (0,1)]
#     cnt = 0
#     cnt_size = [0]

#     # BFS로 덩어리 라벨링
#     for r in range(n):
#         for c in range(m):
#             if grid[r][c] == 1 and visited[r][c] == 0:
#                 cnt += 1
#                 q = deque([(r,c)])
#                 visited[r][c] = 1
#                 grid[r][c] = cnt
#                 size = 1

#                 while q:
#                     x, y = q.popleft()
#                     for dx, dy in dirs:
#                         nx, ny = x+dx, y+dy
#                         if 0 <= nx < n and 0 <= ny < m:
#                             if visited[nx][ny] == 0 and grid[nx][ny] == 1:
#                                 visited[nx][ny] = 1
#                                 grid[nx][ny] = cnt
#                                 size += 1
#                                 q.append((nx, ny))
#                 cnt_size.append(size)

#     # 열(column)별 시추관 계산
#     answer = 0
#     for col in range(m):
#         seen = set()
#         total = 0
#         for row in range(n):
#             bar = grid[row][col]
#             if bar != 0 and bar not in seen:
#                 seen.add(bar)
#                 total += cnt_size[bar]
#         answer = max(answer, total)

#     return answer



