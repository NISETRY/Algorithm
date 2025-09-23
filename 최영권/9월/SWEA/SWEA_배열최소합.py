T = int(input())
answer = 1e9

def dfs(cnt, visited):
    global answer
    if len(picked) == N:
        cur_total = 0
        for i in range(len(arr)):
            cur_total += arr[i][picked[i]]

        if cur_total >= answer:
            return    
        
        answer = min(answer, cur_total)
        return 
    
    for i in range(N):
        if not visited[i]:
            picked.append(lst[i])
            visited[i] = 1
            dfs(cnt+1, visited)
            picked.pop()
            visited[i] = 0

for tc in range(1, T+1):
    N = int(input())
    lst = list(range(N))
    answer = 1e9
    arr = [list(map(int, input().split())) for _ in range(N)]
    picked = []
    visited = [0] * N
    dfs(0, visited)
    print(f"#{tc} {answer}")