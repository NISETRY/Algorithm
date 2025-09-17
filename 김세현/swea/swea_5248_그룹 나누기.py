T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인접 리스트
    group = [[] for _ in range(N+1)]

    for i in range(0, 2*M, 2): 
        a, b = arr[i], arr[i+1]
        group[a].append(b)
        group[b].append(a)

    visited = [False] * (N+1)

    def dfs(node):
        visited[node] = True # 방문 처리
        for n in group[node]:
            if not visited[n]:
                dfs(n)

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(f'#{tc} {cnt}')
