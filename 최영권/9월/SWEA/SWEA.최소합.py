T = int(input())

def dfs(r, c,cur):
    global answer
    if cur >= answer:
        return
    if r == N - 1 and c == N - 1:
        answer = min(answer, cur)
        return

    # 아래로
    if r + 1 < N:
        dfs(r + 1, c, cur + arr[r + 1][c])
    # 오른쪽으로
    if c + 1 < N:
        dfs(r, c + 1, cur + arr[r][c + 1])

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = sum(map(sum, arr))
    total = arr[0][0]
    dfs(0, 0, total)
    print(f"#{tc} {answer}")