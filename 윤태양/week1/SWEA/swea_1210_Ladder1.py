for tc in range(10):
    input()
    graph = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    graph = graph[::-1]
     
    for j in range(len(graph)):
        if graph[0][j] == 2:
            now_r, now_c = 0, j
                 
                 
    while True:
        visited[now_r][now_c] = 1
        if now_r == 99:
            print(f'#{tc+1} {now_c}')
            break
 
        if 0<=now_c+1<100:
            if graph[now_r][now_c+1] == 1 and visited[now_r][now_c+1] == 0:
                now_c += 1
                continue
 
        if 0<=now_c-1<100:
            if graph[now_r][now_c-1] == 1 and visited[now_r][now_c-1] == 0:        
                now_c -= 1
                continue
        now_r +=1