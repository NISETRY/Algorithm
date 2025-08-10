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