T = 10
for tc in range(1, T+1):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # 2찾기, 출발점
    start = 0
    for i in range(100):
        if ladder[99][i] == 2:
            start = i
   
    # 초기값
    x = 99
    y = start

    while x > 0:   
        if y > 0 and ladder[x][y-1] == 1:
            # y를 움직일건데 다음에 0이 나오는 직전까지 가라
            while y > 0 and ladder[x][y-1] == 1:
                y -= 1
           # 왼쪽으로 다 가고 위로 한 칸     
            x -= 1
        
            # 오른쪽
        elif y < 99 and ladder[x][y+1] == 1:
            while y < 99 and ladder[x][y+1] == 1:
                y += 1
            # 오른쪽으로 다 가고 위로 한 칸
            x -= 1
     

        else:
            x -= 1
    print(f"#{tc} {y}")