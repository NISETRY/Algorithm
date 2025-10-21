import pprint

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]

# 처음에 떨어트리기
def drop_first(r, c, h, w):
    """좌상단 (r, c0)에 h×w 박스를 놓을 수 있는지 검사"""
    # 범위 검사
    if r + h > n or c < 0 or c + w > n:
        return False
    
    # 0일때만 떨구기
    for i in range(h):
        for j in range(w):
            if graph[r + i][c + j] != 0:
                return False
    return True

# 택배 쌓아 두기
for _ in range(1, m+1):
    k, h, w, C = map(int, input().split())

    r = 0
    while drop_first(r, C-1, h, w):
        r += 1
    r -= 1
    
    for i in range(h):
        for j in range(w):
            graph[r+i][C-1+j] = k
            pprint.pprint(graph)

# 빼내기
def left_out(grid):
    # 행마다 0이 아닌값이 처음 나온 경우 숫자를 저장
    check = [0] * n 
    for c in range(n):
        for r in range(n):
            
            if grid[r][c] and not check[r]:
                check[r] = (grid[r][c], c)
                print(check)

left_out(graph)