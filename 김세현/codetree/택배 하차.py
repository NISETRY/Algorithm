import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[0]*N for _ in range(N)]
heights = [0]*N                    # 각 열의 바닥부터 누적 높이

# 기본 택배 상자 배치
for _ in range(M):
    k, h, w, c = map(int, input().split())   # 번호, 세로, 가로, 왼쪽열
    c0 = c - 1                            
    base = max(heights[c0:c0+w])              # 착지 높이(바닥부터 칸 수)
    r0 = N - (base + h)                       # 좌상단 행

    # 박스 채우기
    for dr in range(h):
        for dc in range(w):
            grid[r0 + dr][c0 + dc] = k

    # 높이 갱신
    new_h = base + h
    for j in range(c0, c0 + w):
        heights[j] = new_h


# 1. 택배 투입: 모든 상자 입력
# 2. 택배 하차 (좌측): 
# 3. 하차 후 낙하 할 수 있는 택배 낙하
# 4. 택배 하차 (우측):
# 5. 하차 후 낙하 할 수 있는 택배 낙하
# 2~5. 반복 모든 택배가 하차할 때까지

# 1. 
# 상자가 한 칸 아래로 더 내려갈 수 있는지 확인하자
# 아래 한 줄만 확인하면 됨
# def check_fall(r, c, w, h):
#     nr = r + 1
#     if nr + h - 1 >= N: # 바닥 밖이면 못 내려감
#         return False 
#     # 아래가 비었는지 확인
#     for cc in range(c, c+w):
#         if grid[nr + h - 1][cc] != 0:
#             return False
#     return True 

# 사각형 box(r0,c0,r1,c1)가 한 칸 아래로 내려갈 수 있는지 확인
def can_fall(grid, box):
    
    N = len(grid)
    r0, c0, r1, c1 = box
    if r1 + 1 >= N:
        return False
    # 바로 아래 한 줄이 모두 빈칸이어야 함
    for c in range(c0, c1+1):
        if grid[r1+1][c] != 0:
            return False
    return True

# 좌측 하차
def can_exit_left(grid, box):
    r0, c0, r1, c1 = box
    # 세로 구간 r0..r1에 대해 c=0..c0-1이 전부 비어야 하차 가능
    for c in range(0, c0):
        for r in range(r0, r1+1):
            if grid[r][c] != 0:
                return False
    return True

# 우측 하차
def can_exit_right(grid, box):
    N = len(grid)
    r0, c0, r1, c1 = box
    for c in range(c1+1, N):
        for r in range(r0, r1+1):
            if grid[r][c] != 0:
                return False
    return True

