T = int(input())

def dfs(r, c, cur):
    global answer
    if len(picked) == N:
        print(picked)
        for i in range(N):
            print(picked[i], picked[(i+1)%N], arr[picked[i]][picked[(i+1)%N]])
            cur += arr[picked[i]][picked[(i+1)%N]]
        answer = min(answer, cur)
        return
    
    
    for i in range(N):
        if not visited[i]:
            picked.append(i)
            visited[i] = 1
            dfs(c, i, cur)
            picked.pop()
            visited[i] = 0


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 1e10
    total = 0
    picked = [0]
    visited = [0] * N
    visited[0] = 1
    dfs(0, 0, total)
    print(f"#{tc} {answer}")