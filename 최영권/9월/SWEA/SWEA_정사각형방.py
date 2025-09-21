T = int(input())


def dfs(r, c, count, start):
    global answer, start_num
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] - arr[r][c] == 1:
                dfs(nr, nc, count + 1, start)
    if count > answer:
        answer = count
        start_num = start
        # print(answer, start_num)
    elif count == answer:
        if start < start_num:
            start_num = start


for tc in range(1, T + 1):
    N = int(input())
    answer = 0
    start_num = 0
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            dfs(i, j, 1, arr[i][j])

    print(f"#{tc} {start_num} {answer}")