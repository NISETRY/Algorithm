## N-Queens
def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가
    for i in range(row):
        if visited[i][col]:
            return False

    # 2. 좌상단 대각선에 놓은적이 있는가?
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False        
        i -= 1
        j -= 1
    # for i, j in zip(range(row-1,-1,-1), range(col-1,-1,-1)):
        # if visited[i][j]:
        #     return False
    # 3. 우상단 대각선에 놓은적이 있는가?
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False        
        i -= 1
        j += 1
    return True


def recur(row):
    global answer
    if row == N:
        # print(*path)
        answer += 1
        return
    for col in range(N):
        # 가지치기 : 같은 열을 못 고르도록
        # --> 이제는 유망하지 않은 케이스를 모두 삭제(세로, 대각선)
        if check(row, col) is False:   
            continue
        # col을 선택했다
        visited[row][col] = 1
        # path.append(col)
        recur(row + 1)
        # path.pop()
        visited[row][col] = 0



N = 8
answer = 0 # 가능한 정답 수
# path = []   # 임시변수
visited = [[0] * N for _ in range(N)]
# 종료 조건 : N개의 행을 모두 고려하면 종료
# 가지의 수 : N개의 열
recur(0)
print(f"N = {N}, answer = {answer}")


# 트리 : 싸이클이 없는 그래프 (연결 그래프)
# 트리는 싸이클이 없는 무향 연결 그래프
# 두 노드 사이에는 유일한 경로가 존재
# 각 노드는 최대 하나의 부모 노드가 존재
# 각 노드는 자식 노드가 없거나 하나 이상이 존재할 수 있음
