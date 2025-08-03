T= int(input())
for test_case in range(1, T+1):
    sudo_frame = [[0] * 9 for i in range(9)]            # 0으로만 이루어진 9x9 2차원 리스트 생성

    for i in range(9):
        sudo_frame[i] = list(map(int, input().split())) # input 데이터를 각 줄 별로, int로 이뤄진 list로 변환하여 9x9에 넣기


    # 가로행
    row = True
    for i in range(9):
        if set(range(1, 10)) != set(sudo_frame[i]):
            row = False

    # 세로열
    col = True
    for i in range(9):
        if set(range(1, 10)) != set(list(zip(*sudo_frame))[i]):
            col = False

    # 박스형
    box = True
    a = []

    for i in range(1):
        for j in range(3):
            a += sudo_frame[j][3 * i : 3 * i + 3]
        
    check = [0] * 10
    for i in a:
        if check[i] == 0:
            check[i] = 1
        else:
            box = False
            break
    if row and col and box:
        answer = "INCORRECT"
    else:
        answer = "CORRECT"
    if test_case != T:
        input()
    print(f'Case {test_case}: {answer}')