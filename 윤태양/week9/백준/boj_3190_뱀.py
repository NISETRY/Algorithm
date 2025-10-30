from collections import deque

n = int(input())
graph = [[0]*n for _ in range(n)]
swap = deque()
move = [(0,1),(1,0),(0,-1),(-1,0)]

now_r, now_c, delta = 0,0,0
visited = [[0]*n for _ in range(n)]
time = 0
snake = deque([(0,0)])

k = int(input())
for _ in range(k):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 1

l = int(input())
for _ in range(l):
    t, direction = input().split()
    swap.append((int(t), direction))
    
while True:
    nx_r, nx_c = move[delta][0] + now_r, move[delta][1] + now_c
    if not 0<=nx_r<n or not 0<=nx_c<n:
        break
    
    if visited[nx_r][nx_c] == 1:
        break
    
    else:
        if graph[nx_r][nx_c] == 1:
            snake.append((nx_r, nx_c))
            visited[nx_r][nx_c] = 1
            graph[nx_r][nx_c] = 0
            
        else:
            snake.append((nx_r, nx_c))
            visited[nx_r][nx_c] = 1
            t_r, t_c = snake.popleft()
            visited[t_r][t_c] = 0
            
    now_r, now_c = nx_r, nx_c
    time += 1
    
    if swap:
        if time == swap[0][0]:
            if swap[0][1] == 'D':
                delta = (delta+1)%4
                swap.popleft()
                
            elif swap[0][1] == 'L':
                delta = (delta-1)%4
                swap.popleft()

print(time+1)