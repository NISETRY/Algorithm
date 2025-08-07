T = int(input())

for tc in range(T):
    N = int(input())
    result = [[0]*N for _ in range(N)]


    x, y = 0, 0 # 시작 위치
    dir = 'right' # 처음은 오른쪽으로 가니까
    num = 1

    while num <= N*N:
        result[x][y] = num
        num += 1

        # 방향 꺾일 때
        if dir == 'right':
            if y + 1 < N and result[x][y+1] == 0:
                y += 1
            else:
                dir = 'down'
                x += 1
        elif dir == 'down':
            if x + 1 < N and result[x+1][y] == 0:
                x += 1
            else:
                dir = 'left'
                y -= 1
        elif dir == 'left':
            if y - 1 >= 0 and result[x][y-1] == 0:
                y -= 1
            else:
                dir = 'up'
                x -= 1
        elif dir == 'up':
            if x - 1 >= 0 and result[x-1][y] == 0:
                x -= 1
            else: 
                dir = 'right'
                y += 1
    
    print(f'#{tc+1}')
    for row in result:
        print(*row)

