for tc in range(1, 11):
    input()  # 테스트 번호 건너뛰기
    ladders = [list(map(int, input().split())) for _ in range(100)]
    
    # 바닥(99행)에서 도착점(2) 찾기
    x = 99
    for j in range(100):
        if ladders[99][j] == 2:
            y = j
            break

    # 역추적: 맨 위(0행) 도달 전까지
    while x > 0:
        # 왼쪽으로 이동 가능한 경우
        if y > 0 and ladders[x][y-1] == 1:
            while y > 0 and ladders[x][y-1] == 1:
                y -= 1
            x -= 1
        # 오른쪽으로 이동 가능한 경우
        elif y < 99 and ladders[x][y+1] == 1:
            while y < 99 and ladders[x][y+1] == 1:
                y += 1
            x -= 1
        # 그 외에는 위로 한 칸
        else:
            x -= 1

    # 최종 y가 출발점 X좌표
    print(f'#{tc} {y}')
