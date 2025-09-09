from collections import deque

def bfs(a,b):
    global max_apple
    visited[0][0][0][0] = 1
    que = deque([(a,b,0,0,0,0)]) # r,c,apple,dir,cnt,is_turn
    min_cnt = 999
    count = 0
    while que:
        count += 1
        x,y,apple,dir,cnt,is_turn = que.popleft()

        if cnt > min_cnt and apple < max_apple:
            continue

        if graph[x][y] == num_apple and apple+1 == num_apple:
            min_cnt = min(min_cnt, cnt)
            max_apple = max(apple+1, max_apple)
            continue

        if graph[x][y] == apple + 1:
            que.append((x,y,apple+1,dir,cnt,is_turn))
            max_apple = max(apple+1, max_apple)

        if is_turn == 0:
            # visited[(dir+1)%4][apple][x][y] = 1
            que.append((x,y,apple,(dir+1)%4,cnt+1,is_turn+1))

            nx, ny = x+move[dir][0], y+move[dir][1]
            if 0<=nx<n and 0<=ny<n:
                if visited[dir][apple][nx][ny] == 0:
                    visited[dir][apple][nx][ny] = 1
                    que.append((nx,ny,apple,dir,cnt,is_turn))
           
        else:
            nx, ny = x+move[dir][0], y+move[dir][1]
            if 0<=nx<n and 0<=ny<n:
                if visited[dir][apple][nx][ny] == 0:
                    visited[dir][apple][nx][ny] = 1
                    que.append((nx,ny,apple,dir,cnt,is_turn-1))

    return min_cnt

t = int(input())
move = [[0,1],[1,0],[0,-1],[-1,0]] 

for tc in range(t):
    n = int(input())
    num_apple = 0
    max_apple = -1
    graph = [list(map(int, input().split())) for _ in range(n)]
    num_apple += sum(1 for i in range(n) for j in range(n) if graph[i][j] != 0)
    visited = [[[[0 for _ in range(n)] for _ in range(n)] for _ in range(num_apple)] for _ in range(4)] # dir/apple/x/y

    print(bfs(0,0))

    # print(visited[3][2][4][4])


    