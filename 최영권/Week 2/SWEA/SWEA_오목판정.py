# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())

#     arr = [input() for _ in range(N)]
    
    
#     max_row = 0
#     max_col = 0
    

#     # 가로
#     for r in range(N):
#         row_sum = 0
#         for c in range(N):
#             if arr[r][c] == 'o':
#                 row_sum += 1
#             else:
#                 row_sum = 0

#             max_row = max(row_sum, max_row)
    
#     # 세로
#     for col in zip(*arr):
#         col_sum = 0
        
#         for j in range(N):
#             if col[j] == 'o':
#                 col_sum += 1
#             else:
#                 col_sum = 0

#             max_col = max(col_sum, max_col)

#     # 대각선

#     dr = [1, -1]
#     dc = [1, -1]
#     cnt_left_right = 0
#     for r in range(2, N-1):
#         for c in range(2, N-1):
            
#             if arr[r][c] == 'o':
#                 cnt = 1
#                 for dist in range(1, 3):
#                     for d in range(2):
#                         nr = r + dr[d]*dist
#                         nc = c + dc[d]*dist
#                         if 0<=nr<=N-1 and 0<=nc<=N-1 and arr[nr][nc] =='o':
#                             cnt += 1

#                 cnt_left_right = max(cnt_left_right, cnt)
            
#     dr = [-1, 1]
#     dc = [1, -1]
#     cnt_right_left = 0
#     for r in range(2, N-1):
#         for c in range(2, N-1):
            
#             if arr[r][c] == 'o':
#                 cnt = 1
#                 for dist in range(1, 3):
#                     for d in range(2):
#                         nr = r + dr[d]*dist
#                         nc = c + dc[d]*dist
#                         if 0<=nr<=N-1 and 0<=nc<=N-1 and arr[nr][nc] =='o':
#                             cnt += 1

#                 cnt_right_left = max(cnt_right_left, cnt)
#     if max(max_row, max_col, cnt_left_right, cnt_right_left) >= 5:
#         print(f"#{tc} YES")
#     else:
#         print(f"#{tc} NO")              
dr = [-1, 0, 1, 1, 1, 0, -1, -1]
dc = [1, 1, 1, 0, -1, -1, -1, 0]
def check(arr, r, c):
    for i in range(8):
        cnt = 1
        nr = r + dr[i]
        nc = c + dc[i]
        while 0<=nr<N and 0<=nc<N and arr[nr][nc] == 'o':
            nr = r + dr[i]
            nc = c + dc[i]
            cnt += 1
        if cnt == 5: 
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    ans = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                if check(arr, i, j):
                    ans = 'YES'
    print(f"#{tc} {ans}")
                       
    print()