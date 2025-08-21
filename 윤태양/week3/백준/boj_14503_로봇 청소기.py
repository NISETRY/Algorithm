n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
move = [[-1,0],[0,1],[1,0],[0,-1]] #북동남서 
cnt = 0
Flag = False

def back(r,c,d): # 후진
    global Flag
    dx, dy = move[(d+2)%4][0], move[(d+2)%4][1]
    nx, ny = r+dx, c+dy

    if graph[nx][ny] == 1:
        Flag = True
        return r,c,d

    else:
        return nx, ny, d

def left_forward(r,c,d): # 왼쪽 회전 + 전진
    global cnt 
    d = d-1
    if d == -1:
        d = 3

    nx, ny = r+move[d][0], c+move[d][1]

    if graph[nx][ny] == 0 and visited[nx][ny] == 0:
        return nx,ny,d
    else:
        return r,c,d

def search(r,c): # 4방향 탐색 
    for dx,dy in move:
        nx,ny = r+dx,c+dy
        if graph[nx][ny] == 0 and visited[nx][ny] == 0:
            return True
    return False

while True:
    if Flag == True:  # 벽 만났을 때
        print(cnt)
        break

    if graph[r][c] == 0 and visited[r][c] == 0: # 청소
        visited[r][c] = 1
        cnt += 1
        continue

    if search(r,c):
        r,c,d = left_forward(r,c,d)

    else:
        r,c,d = back(r,c,d)
    

