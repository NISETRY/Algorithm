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
    r = 99 # 맨 아래 행 (99번 인덱스)
    c = ladder[99].index(2) # 2가 있는 열 찾기

    dir = 0 # 처음엔 위로 이동
    while r > 0: # 맨 윗줄까지 갈 때까지
        for i in range(len(search_dir[dir])): 
            # 다음 방향 후보
            next_dir = search_dir[dir][i] # 우선순위에 따라 다음 방향 선택
            next_r = r+dr[next_dir] # 다음 행 좌표
            next_c = c+dc[next_dir] # 다음 열 좌표

            if 0 <= next_c < 100 and ladder[next_r][next_c] == 1:
                # 범위 안에 있고, 길이 있는 경우에 이동
                dir = next_dir
                r = next_r
                c = next_c
                break

    print(f'#{tc} {c}') 

