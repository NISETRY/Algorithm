from collections import deque

def bfs(a,b):
    global answer, ans_idx

    que = deque([(a,b)])
    count = 1
    idx = graph[a][b]

    while que:
        x,y = que.popleft()

        for dx,dy in move:
            nx,ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] -1 == graph[x][y]:
                    que.append((nx,ny))
                    count += 1

    if count == answer:
        if idx < ans_idx:
            answer, ans_idx = count, idx

    if count > answer:
        answer,ans_idx = count, idx
    
t = int(input())

for tc in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = -1
    ans_idx = 9999999999
    move = [[-1,0],[1,0],[0,1],[0,-1]]
    for i in range(n):
        for j in range(n):
            if answer + graph[i][j] > n**n:
                continue
            bfs(i,j)

    print(f'#{tc+1} {ans_idx} {answer}')