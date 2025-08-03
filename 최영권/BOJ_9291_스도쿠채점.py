T =  int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    
    for r in range(9):
        row = set()
        col = set()
        for c in range(9):
            row.add(sudoku[r][c])
            col.add(sudoku[c][r])  
            if (r % 3 == 0) and (c % 3 == 0):
                square = set() 
                for x in range(3):
                    for y in range(3):
                    # print(r, c, x, y)
                        square.add(sudoku[r+x][c+y])
        if len(row) != 9 or len(col) != 9 or len(square) != 9:
            print(f"Case {tc}: INCORRECT")     
            break   
    else:
        print(f"Case {tc}: CORRECT")

    if tc != T:
        input()