# 0 : 상, 1 : 좌, 2 : 우
dr = [-1, 0, 0]
dc = [0, -1, 1]

# 0 : [1, 2, 0]
# 1 : [0, 1]
# 2 : [0, 2]
search_dir = [[1, 2, 0], [0, 1], [0,2]]

T = 10

for tc in range(1, T+1):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    r = 99
    c = ladder[99].index(2)

    dir = 0
    while r > 0:
        for i in range(len(search_dir[dir])):
            # 다음 방향 후보
            next_dir = search_dir[dir][i]
            next_r = r+dr[next_dir]
            next_c = c+dc[next_dir]

            if 0 <= next_c < 100 and ladder[next_r][next_c] == 1:
                dir = next_dir
                r = next_r
                c = next_c
                break

    print(f'#{tc} {c}') 

