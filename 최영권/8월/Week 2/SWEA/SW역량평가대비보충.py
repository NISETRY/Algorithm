# SWEA 9386 연속한 1의 개수

# T = int(input())

# for tc in range(1, T+1):
#     input()
#     lst = list(map(int, input()))
#     num_of_ones = 0
#     max_ones = 0
#     for i in range(len(lst)):
        
#         if lst[i] == 0:
#             num_of_ones = 0
#         elif lst[i] == 1:
#             num_of_ones += 1
#             if max_ones < num_of_ones:
#                 max_ones = num_of_ones
#     print(f"#{tc} {max_ones}")

# SWEA 20397 돌 뒤집기 게임 2
# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())

#     lst = list(map(int, input().split()))
#     for x in range(M):
#         i, j = map(int, input().split())
#         i = i-1
#         for dist in range(1, j+1):
#             if i - dist < 0 or i + dist > (N-1):
#                 break
#             elif lst[i-dist] == lst[i+dist]:
#                 lst[i-dist], lst[i+dist] = 1- lst[i-dist], 1- lst[i+dist]
#             elif lst[i-dist] != lst[i+dist]:
#                 continue
#     print(f"#{tc}", *lst)

# 스위치 조작
# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())

#     before = list(map(int, input().split()))
#     after = list(map(int, input().split()))
#     count = 0
#     for i in range(N):
#         if before[i] == after[i]:
#             continue
#         else:
#             for j in range(i+1, N):
#                 before[j] = 1 - before[j]
#             count += 1
    
#     print(f"#{tc} {count}")

# 풍선팡 보너스게임
# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())

#     ballon = [list(map(int, input().split())) for _ in range(N)]

#     max_sum = 0
#     for r in range(len(ballon)):
#         for c in range(len(ballon[r])):
            
#             cur_sum = ballon[r][c]
#             for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
#                 for length in range(1, N):
#                     nr = r+ dr*length
#                     nc = c+ dc*length
#                     if 0<=nr<=N-1 and 0<=nc<=N-1:
#                         cur_sum += ballon[nr][nc]

#             if cur_sum > max_sum:
#                 max_sum = cur_sum
#     print(f"#{tc} {max_sum}")        


# SWEA 9386 연속한 1의 개수

# T = int(input())

# for tc in range(1, T+1):
#     input()
#     lst = list(map(int, input()))
#     num_of_ones = 0
#     max_ones = 0
#     for i in range(len(lst)):
        
#         if lst[i] == 0:
#             num_of_ones = 0
#         elif lst[i] == 1:
#             num_of_ones += 1
#             if max_ones < num_of_ones:
#                 max_ones = num_of_ones
#     print(f"#{tc} {max_ones}")

# SWEA 20397 돌 뒤집기 게임 2
# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())

#     lst = list(map(int, input().split()))
#     for x in range(M):
#         i, j = map(int, input().split())
#         i = i-1
#         for dist in range(1, j+1):
#             if i - dist < 0 or i + dist > (N-1):
#                 break
#             elif lst[i-dist] == lst[i+dist]:
#                 lst[i-dist], lst[i+dist] = 1- lst[i-dist], 1- lst[i+dist]
#             elif lst[i-dist] != lst[i+dist]:
#                 continue
#     print(f"#{tc}", *lst)

# 스위치 조작
# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())

#     before = list(map(int, input().split()))
#     after = list(map(int, input().split()))
#     count = 0
#     for i in range(N):
#         if before[i] == after[i]:
#             continue
#         else:
#             for j in range(i+1, N):
#                 before[j] = 1 - before[j]
#             count += 1
    
#     print(f"#{tc} {count}")

# 풍선팡 보너스게임
# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())

#     ballon = [list(map(int, input().split())) for _ in range(N)]

#     max_sum = 0
#     for r in range(len(ballon)):
#         for c in range(len(ballon[r])):
            
#             cur_sum = ballon[r][c]
#             for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
#                 for length in range(1, N):
#                     nr = r+ dr*length
#                     nc = c+ dc*length
#                     if 0<=nr<=N-1 and 0<=nc<=N-1:
#                         cur_sum += ballon[nr][nc]

#             max_sum = max(cur_sum, max_sum)
#     print(f"#{tc} {max_sum}")        

# 고대 유적2
# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())

#     pyramid = [list(map(int, input().split())) for _ in range(N)]

#     # 가로 방향으로 연속된 1의 개수
#     vertical_max = 0
#     for r in range(N):
#         cur_length = 0
#         for c in range(M):
#             if pyramid[r][c] == 1:
#                 cur_length += 1 
#                 vertical_max = max(vertical_max, cur_length)
#             else:
#                 cur_length = 0
    
#     # 세로 방향으로 연속된 1의 개수
#     horizontal_max = 0
#     for c in range(M):  # 열의 개수만큼 반복
#         cur_length = 0
#         for r in range(N):  # 행을 순회하면서 세로 방향 확인
#             if pyramid[r][c] == 1:
#                 cur_length += 1 
#                 vertical_max = max(vertical_max, cur_length)
#             else:
#                 cur_length = 0
#     answer = max(vertical_max, horizontal_max)
#     if answer == 1:
#         answer = 0
#     print(f"#{tc} {answer}")

    
# 강사님 스위치 조작
# T = int(input())
# def reverse(source, start):
#     for i in range(start, N):
#         source[i] ^= 1  # source[i] = source[i] ^ 1
# for tc in range(1, T+1):
#     N = int(input())
#     source = list(map(int, input().split()))
#     target = list(map(int, input().split()))
#     cnt = 0
#     for i in range(N):   # source를 순회
#         if source[i] == target[i]:
#             continue
#         reverse(source, i)
#         cnt += 1
#     print(f"#{tc} {cnt}")

# 강사님 풍선팡
# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())

#     ballon = [list(map(int,input().split())) for _ in range(N)]
#     max_v = 0
#     for i in range(N):
#         for j in range(N):
#             sum_v = 0
#             for k in range(N):
#                 sum_v += ballon[i][k]
            
#             for k in range(N):
#                 sum_v += ballon[k][j]
#             sum_v -= ballon[i][j]
#             max_v = max(sum_v, max_v)
#     print(f"#{tc} {max_v}")

# IM시험 빈출 -> 델타!!
def find_pos(a):
    for i in range(N):
        for j in range(N):
            if a[i][j] == 2:
                return i, j

def solve(a,r,c):
    
    for i in range(4):           # 방향을 먼저
        for j in range(1, N):    # 광선의세기
            nr = r + dr[i] * j
            nc = c + dc[i] * j   
            if 0<=nr<N and 0<=nc<N:
                if arr[nr][nc] == 1:
                    break
                else:
                    arr[nr][nc] = 9  # 방문체크

def ge_count(a):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if a[i][j] == 0:
                cnt+= 1
    return cnt

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 1. 괴물 위치 찾기
    r,c = find_pos(arr)
    # 2. 괴물의 좌표로 4방향 탐색
    solve(arr, r, c)

    
    # 3. 빛이 안 온 셀의 갯수
    ans = ge_count(arr)
    print(f"#{tc} {ans}")