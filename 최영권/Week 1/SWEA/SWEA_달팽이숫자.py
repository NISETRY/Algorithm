T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    # direction
    dir_x = [1, 0, -1, 0]
    dir_y = [0, 1, 0, -1]

    # time
    time = []
    for t in range(N):
        time.append(N-t)
        time.append(N-t)
    time.remove(N)

    # 초기값
    x, y = -1, 0
    dir = 0
    num = 1
    
    for t in time:
        for _ in range(t):
            x += dir_x[dir]
            y += dir_y[dir]
            arr[y][x] = num
            num += 1
        dir = (dir+1)%4
    print(f"#{tc}")

    for r in arr:
        for c in r:
            print(c, end =' ')
        print()
