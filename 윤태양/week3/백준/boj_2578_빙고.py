graph = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
call2 = []
now = 0
bingo = 0

for i in range(5):
    for j in range(5):
        call2.append(call[i][j])

for _ in range(25):
    bingo = 0

    for r in range(5):
        for c in range(5):
            if graph[r][c] == call2[now]:
                graph[r][c] = -1

    for x in range(5): # 행검사
        row = 0
        for y in range(5):
            row += graph[x][y]
        if row == -5:
            bingo += 1

    for x in range(5): # 열검사
        col = 0
        for y in range(5):
            col += graph[y][x] 
        if col == -5:
            bingo += 1
    i_j = 0
    for x in range(5):   #우각선검사
        for y in range(5):
            if x == y:
                i_j += graph[x][y]
                if i_j == -5:
                    bingo += 1
    j_i = 0
    for x in range(5):   #좌각선검사
        for y in range(5):
            if 4-x == y: 
                j_i += graph[x][y] 
                if j_i == -5:
                    bingo += 1
    if bingo >= 3:
        print(now+1)
        exit()

    now += 1
