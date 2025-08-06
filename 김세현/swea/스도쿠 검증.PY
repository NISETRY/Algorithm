puzzle = []

for _ in range(9):
    row = list(map(int, input().split()))
    puzzle.append(row)

# 행 확인
for row in puzzle:
    if len(set(row)) != 9:
        print("행 중복")
        break

# 열 확인
for col in range(9):
    column = []
    for row in range(9):
        column.append(puzzle[row][col])

    print(column)



# 행 확인
# 열 확인
# 3X3 확인