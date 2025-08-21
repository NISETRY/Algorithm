# # Flatten
# for tc in range(10):

#     dump = int(input()) # 덤프 횟수
#     box = list(map(int, input().split()))

#     for i in range(dump):
#         box[box.index(max(box))] = max(box) - 1
#         box[box.index(min(box))] = min(box) + 1

#     print(f'#{tc+1} {max(box) - min(box)}')



# # 파리 퇴치 복습
# T = int(input())

# for tc in range(T):

#     N, M = map(int, input().split())

#     arr = [list(map(int, input().split())) for _ in range(N)]

#     max_sum = 0

#     # 시작점 할당
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             sum = 0
#             for x in range(M):
#                 for y in range(M):
#                     sum += arr[i+x][j+y]

#             if sum > max_sum:
#                 max_sum = sum

#     print(f'#{tc+1} {max_sum}')

# # 파리 퇴치3
# T = int(input())

# for tc in range(T):

#     N, M = map(int, input().split())

#     arr = [list(map(int, input().split())) for _ in range(N)]

#     max_sum = 0
#     dir_plus = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     dir_x = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

#     for i in range(N):
#         for j in range(N):

#         # + 모양
#             plus_sum = arr[i][j] # 중심

#             for dx, dy in dir_plus:
#                 for d in range(1, M):
#                     nx = i + dx * d
#                     ny = j + dy * d
#                     if 0 <= nx < N and 0 <= ny < N:
#                         plus_sum += arr[nx][ny]
#                     else:
#                         break
        
#         # X 모양
#             x_sum = arr[i][j] # 중심

#             for dx, dy in dir_x:
#                 for d in range(1, M):
#                     nx = i + dx * d
#                     ny = j + dy * d
#                     if 0 <= nx < N and 0 <= ny < N:
#                         x_sum += arr[nx][ny]
#                     else:
#                         break

#         max_sum = max(max_sum, plus_sum, x_sum)
    
#     print(f'#{tc+1} {max_sum}')

# # sum
# arr = [list(map(int, input().split())) for _ in range(100)]

# # 행 합
# row_sum = 0

# for i in range(100):
#     sum = 0
#     for j in range(100):
#         sum += arr[i][j]

#     if row_sum < sum:
#         row_sum = sum

# # 열 합
# col_sum = 0

# for j in range(100):
#     sum = 0
#     for i in range(100):
#         sum += arr[i][j]

#     if col_sum < sum:
#         col_sum = sum

# # 대각선 합
# max_sum1 = 0
# max_sum2 = 0
# for i in range(100):
#     max_sum1 += arr[i][i]
#     max_sum2 += arr[i][99-i]

# # 파리 퇴치
# T = int(input())

# for tc in range(T):

#     N, M = map(int, input().split())

#     arr = [list(map(int, input().split())) for _ in range(N)]

#     max_sum = 0

#     # 시작점 할당
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             sum = 0
#             for x in range(M):
#                 for y in range(M):
#                     sum += arr[i+x][j+y]

#             if max_sum < sum:
#                 max_sum = sum
        
#     print(f'#{tc+1} {max_sum}')
    
# # 어디에 단어가 들어갈 수 있을까
# N, K = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(N)]

# # 가로 확인하기
# col_sum = 0
# result_col = 0

# for i in range(N):
#     count_c = 0
#     for j in range(N):
#         if arr[i][j] == 1:
#                 count_c += 1
        
#         if arr[i][j] == 0 or j == N-1:
#             if count_c == K:
#                 result_col += 1

#             count_c = 0


# # 세로 확인하기
# row_sum = 0
# result_row = 0

# for i in range(N):
#     count_r = 0
#     for j in range(N):
#         if arr[j][i] == 1:
#                 count_r += 1
        
#         if arr[j][i] == 0 or j == N-1:
#             if count_r == K:
#                   result_row += 1

#             count_r = 0

# print(result_row + result_col)


# # 파리퇴치 3
# N, M = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(N)]

# max_sum = 0
# dir_plus = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# dir_x = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# for i in range(N):
#     for j in range(N):

#     # + 모양
#         plus_sum = arr[i][j] # 중심

#         for dx, dy in dir_plus:
#             for d in range(1, M):
#                 nx = i + dx * d
#                 ny = j + dy * d
#                 if 0 <= nx < N and 0 <= ny < N: # 범위 안에서만
#                     plus_sum += arr[nx][ny]
#                 else:
#                     break

#     # X 모양
#         x_sum = arr[i][j]

#         for dx, dy in dir_x:
#             for d in range(1, M):
#                 nx = i + dx * d
#                 ny = j + dy * d
#                 if 0 <= nx < N and 0 <= ny < N:
#                     x_sum += arr[nx][ny]
#                 else:
#                     break

#         max_sum = max(max_sum, plus_sum, x_sum)

# N, M = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(N)]

# max_sum = 0
# dir_plus = [(-1,0), (1,0), (0,-1), (0,1)]
# dir_x = [(-1,-1), (1,1), (-1,1), (1, -1)]


# for i in range(N):
#     for j in range(N):
#         # + 모양
#         plus_sum = arr[i][j]
#         for dx, dy in dir_plus:
#             for d in range(1, M):
#                 nx = i + dx * d
#                 ny = j + dy * d
#                 if 0 <= nx < N and 0 <= ny < N:
#                     plus_sum += arr[nx][ny]
#                 else:
#                     break

#         # x 모양
#         x_sum = arr[i][j]
#         for dx, dy in dir_x:
#             for d in range(1, M):
#                 nx = i + dx * d
#                 ny = j + dy * d
#                 if 0 <= nx < N and 0 <= ny < N:
#                     plus_sum += arr[nx][ny]
#                 else:
#                     break

# # 파리 퇴치 3 
# N, M = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(N)]

# max_sum = 0
# dir_plus = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# dir_x = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# for i in range(N):
#     for j in range(N):
#         # + 모양
#         sum_plus = arr[i][j]
#         for dx, dy in dir_plus:
#             for d in range(1, M):
#                 nx = i + dx * d
#                 ny = j + dy * d
#                 if 0 <= nx < N and 0 <= ny < N:
#                     sum_plus += arr[nx][ny]
#                 else:
#                     break

#         if max_sum < sum_plus:
#             max_sum = sum_plus

#         # X 모양
#         sum_x = arr[i][j]
#         for dx, dy in dir_x:
#             for d in range(1, M):
#                 nx = i + dx * d
#                 ny = j + dy * d
#                 if 0 <= nx < N and 0 <= ny < N:
#                     sum_x += arr[nx][ny]
#                 else:
#                     break

#         if max_sum < sum_x:
#             max_sum = sum_x

# print(max_sum)

T = int(input())

for tc in range(T):
        
    N = int(input())

    arr = [[0] * N for _ in range(N)] # 빈 리스트 만들기

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    x = 0
    y = 0

    move = 0 # 처음은 오른쪽으로 이동

    for i in range(1, N*N+1):
        arr[x][y] = i

        x += di[move]
        y += dj[move]

        # 방향을 바꾸는 조건
        if x < 0 or y < 0 or x >= N or y >= N or arr[x][y] != 0:
            x -= di[move]
            y -= dj[move]

            move = (move + 1) % 4

            x += di[move]
            y += dj[move]

    print(f'#{tc+1}')
    for row in arr:
        print(*row)
