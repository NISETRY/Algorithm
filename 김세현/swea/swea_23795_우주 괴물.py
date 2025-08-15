# N = int(input())

# arr = [list(map(int, input().split())) for _ in range(N)]

# # 0인 칸 수에서 직사광선이 닿지 않는 칸 수를 빼주기

# boss = 0 # 괴물 위치 찾기
# max = 0
# max_pos = (0,0)

# for i in range(N):
#     for j in range(N):
#         if arr[i][j] > max:
#             max = arr[i][j]
#             max_pos = (i,j)
T = int(input())

for tc in range(T):
         
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]           


    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    count = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    for k in range(1, N):
                        nx = i + dx * k
                        ny = j + dy * k

                        if nx < 0 or nx >= N or ny < 0 or ny >= N :
                            break
                        else:
                            if arr[nx][ny] == 1:
                                break
                            if arr[nx][ny] == 0:
                                arr[nx][ny] = 3 # 직사광선이 닿는 칸은 다른 값으로 바꿔주기

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                count += 1

    print(f'#{tc+1} {count}')





                            
