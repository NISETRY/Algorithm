T = int(input())

for tc in range(1, T+1):
    N = int(input())


    matrix = [[0] * N for _ in range(N)]
    # direction
    direction_x = [1, 0, -1, 0]
    direction_y = [0, 1, 0, -1]

    # 반복 횟수 time
    time = []
    for t in range(N):
        time.append(N-t)
        time.append(N-t)
    time.remove(N)

    # 초기 값 세팅
    dir = 0
    num = 1
    x,y = -1, 0

    for t in time:
        for _ in range(t):
            x += direction_x[dir]
            y += direction_y[dir]
            matrix[y][x] = num
            num += 1
        dir = (dir+1) % 4

    print(f"#{tc}")
    for row in range(N):
        for col in range(N):
            print(matrix[row][col], end=' ')
        print()