T = int(input())

for tc in range(1, T+1):

    sudoku = [list(map(int,input().split())) for _ in range(9)]

    # 행, 열
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            row.add(sudoku[i][j])
            col.add(sudoku[j][i])
            if (i % 3 == 0) and (j % 3 == 0):
                box = set()
                for x in range(3):
                    for y in range(3):
                        box.add(sudoku[x+i][y+j])

        if len(row) != 9 or len(col) != 9 or len(box) != 9:
            print(f"#{tc} 0")
            break
    else:
        print(f"#{tc} 1")
