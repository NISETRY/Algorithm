# # 파리 퇴치 복습

# N, M = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(N)]

# max_kill = 0

# for i in range(N-M+1):
#     for j in range(N-M+1):
#         num = 0
#         for x in range(i, i+M):
#             for y in range(j, j+M):
#                 num += arr[x][y]

#         if num > max_kill:
#             max_kill = num

# print(max_kill)


# # SUM 다시 풀어보기

# arr = [list(map(int, input().split())) for _ in range(100)]

# max_result = 0 # 최대값을 0으로 저장해 놓기

# # 행 (가로)
# for row in arr:
#     a = sum(row)
#     if a > max_result:
#         max_result = a

# # 열 (세로)
# for j in range(100):
#     col_sum = 0
#     for i in range(100):
#         col_sum += arr[i][j]
#     if col_sum > max_result:
#         max_result = col_sum

# # 대각선
# D1 = 0
# D2 = 0
# for i in range(100):
#     D1 += arr[i][i]
#     D2 += arr[i][99-i]

# max_result = max(max_result, D1, D2)

