## N-Queens
def check(row):
    for prev_row in range(row):
        # 세로 체크
        if visited[row] == visited[prev_row]:
            return False

        # 열과 행의 차이가 같다 == 현재 col 의 좌우 대각선이다
        # visited 에 저장된 값 = 어느 col에 두었는 가 ?
        # row - prev_row = 행의 차이
        # visited[row] - visited[prev_row] = 열의 차이
        # 이 두 개가 같으면 대각선
        if abs(row - prev_row) == abs(visited[row] - visited[prev_row]):
            return False

    return True



def dfs(row):
    global answer
    if row == N:
        # print(*path)
        answer += 1
        return
    for col in range(N):
        # col을 선택했다
        visited[row] = col  # 현재 row의 col에 놓았다 라고 가정하고
        if not check(row):
            continue
        dfs(row + 1)
    



N = 8
answer = 0 # 가능한 정답 수
# path = []   # 임시변수
visited = [[0] * N for _ in range(N)]
# 종료 조건 : N개의 행을 모두 고려하면 종료
# 가지의 수 : N개의 열
dfs(0)
print(f"N = {N}, answer = {answer}")