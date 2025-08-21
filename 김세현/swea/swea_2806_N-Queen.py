# visited 열 번호로 세팅 v[열] = 1 // 열 검사
T = int(input())

def n_queen(row):
    global answer 

    if row == N:
        answer += 1
        return
    
    for col in range(N):
        # 세로 검사 통과 & 좌하향 통과 & 우하향 통과
        if col_visited[col] == 0 and main_diag_visited[row-col+N-1] == 0 and sub_diag_visited[row+col] == 0:
            col_visited[col] = 1
            main_diag_visited[row-col+N-1] = 1
            sub_diag_visited[row+col] = 1

            n_queen(row+1)

            col_visited[col] = 0
            main_diag_visited[row-col+N-1] = 0
            sub_diag_visited[row+col] = 0

for tc in range(1, T+1):
    N = int(input())

    col_visited = [0]*N
    main_diag_visited =[0]*(2*N-1)
    sub_diag_visited =[0]*(2*N-1)
    answer = 0

    n_queen(0)

    print(f'#{tc} {answer}')