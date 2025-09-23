n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 행 사다리 놓기

count = 0
saro = 0.01

for i in range(n):
    prev = graph[i][0]
    count = 1

    for j in range(n):
        
        if prev != graph[i][j]:

            if prev > graph[i][j] and count >= l and n-l-j >= 0:   # 이전이 낮을 때
                for k in range(1, l+1):
                    graph[i][j-k] += saro
                count = 0 
        else:
            count += 1

        prev = graph[i][j]
        

    if count >= l:
        for k in range(1, l+1):
            if 0<= j-count+k <n:
                graph[i][j-count+k] += saro

    saro = 0.01

print(graph)