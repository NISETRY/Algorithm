n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)] # 내구도 무게
ans = 0

def dfs(now, eggs):
    global ans

    if now == n:
        broken = 0

        for egg in eggs:
            if egg[0] <= 0:
                broken += 1
        ans = max(ans, broken)
        return
    
    if eggs[now][0] <= 0:
        dfs(now+1, eggs)
        return

    hit = False
    for i in range(n):
        if i == now: continue

        if eggs[i][0] <= 0:
            continue
        
        hit = True

        eggs[now][0] -= eggs[i][1]
        eggs[i][0] -= eggs[now][1]
        dfs(now+1, eggs)
        eggs[now][0] += eggs[i][1]
        eggs[i][0] += eggs[now][1]
    
    if not hit:
        dfs(now+1, eggs)
        
dfs(0, eggs)
print(ans)