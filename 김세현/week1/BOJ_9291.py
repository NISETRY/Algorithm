T = int(input())

for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    is_valid = True # 잘못 된 부분이 발견되면 False

    # 행 검사
    for row in puzzle:
        if len(set(row)) != 9:
            is_valid = False
            break

    # 열 검사
    if is_valid:
        for col in range(9):
            column = [puzzle[row][col] for row in range(9)]
            if len(set(column)) != 9:
                is_valid = False
                break
        
        # for col in range(9):
        #     column = []
        #     for row in range(9):
        #         column.append(puzzle[row][col])

    # 3x3 검사
    if is_valid:
        for i in range(0, 9, 3): # 0, 3, 6
            for j in range(0, 9, 3):
                block = []
                for x in range(3):
                    for y in range(3):
                        block.append(puzzle[i+x][j+y])
                if len(set(block)) != 9:
                    is_valid = False
                    break
            if not is_valid:
                break

    # 최종 출력
    if is_valid:
        print(f'Case {tc}: CORRECT')
    else:
        print(f'Case {tc}: INCORRECT')

    # 테스트 케이스 사이에 빈 줄이 있어서 공백 넣어주기 **
    if tc != T:
        input()