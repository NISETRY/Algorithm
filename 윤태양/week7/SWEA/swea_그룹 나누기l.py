def bfs(a):
    visited[a] = 1
    que = [a]

    while que:
        x = que.pop(0)

        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                que.append(i)
                

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    union = list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]    
    graph = [[] for _ in range(n+1)]
    answer = 0 


    for i in range(0,len(union),2):
        graph[union[i]].append(union[i+1])
        graph[union[i+1]].append(union[i])

    for j in graph:
        if j:
            for l in j:
                if not visited[l]:
                    bfs(l)
                    answer += 1

    print(f'#{tc+1} {answer+1}')