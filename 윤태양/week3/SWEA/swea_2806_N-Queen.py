def n_queen(row):
    global answer
    if row == n:
        answer += 1
        return

    for col in range(n):
        if col_visited[col] == 0 and right_diag[row-col+n-1] == 0 and left_diag[col+row] == 0:
            col_visited[col] = 1
            right_diag[row-col+n-1] = 1 
            left_diag[col+row] = 1

            n_queen(row+1)

            col_visited[col] = 0
            right_diag[row-col+n-1] = 0
            left_diag[col+row] = 0
            
t = int(input())

for tc in range(t):
    n = int(input())

    col_visited = [0] * n
    right_diag = [0] * (2*n-1)
    left_diag = [0] * (2*n-1)
    answer = 0

    n_queen(0)
    print(f'#{tc+1} {answer}')