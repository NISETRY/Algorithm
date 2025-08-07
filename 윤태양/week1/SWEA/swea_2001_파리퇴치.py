t = int(input())
 
for tc in range(t):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    max_kill = 0 
         
    for i in range(n-m+1):
        for j in range(n-m+1):
            kill = 0
            for x in range(m):
                for y in range(m):
                    kill += graph[i+x][j+y]
                     
            max_kill = max(max_kill, kill)
    print(f'#{tc+1} {max_kill}')