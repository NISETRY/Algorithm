N, M = map(int, input().split())


picked = []

def dfs():
    if len(picked) == M:
        print(*picked)
    

    else:
        for i in range(1, N+1):
            picked.append(i)
            dfs()
            picked.pop()
    
dfs()