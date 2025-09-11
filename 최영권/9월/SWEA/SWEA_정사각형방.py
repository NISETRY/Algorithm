T = int(input())

def dfs(r, c, count):
    global answer
    for dr,dc in [(1,0), (0,1),(-1,0),(0,-1)]:
        nr, nc = r+dr, c+dc
        if nr<0 or nr >= N or nc<0 or nc>=N:
            continue
        if arr[nr][nc] != arr[r][c] + 1 :
            continue
        print(nr, nc, count)
        dfs(nr, nc, count+1)
    answer = max(answer, count)
    return answer

for tc in range(1, T+1):
    N = int(input())
    answer = 0
    number = N ** 2
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(i, j)
            print(dfs(i, j, 1))
            
    print(f"#{tc} {answer}")