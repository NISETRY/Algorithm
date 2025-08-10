# 파리퇴치3
# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())

#     fly = [list(map(int, input().split())) for _ in range(N)]

#     # +
#     max_t = 0
#     for r in range(N):
#         for c in range(N):
#             cur_sum = fly[r][c]
#             for length in range(1, M):
#                 for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
#                     nr = r + dx*length
#                     nc = c + dy*length

#                     if 0<= nr <= N-1 and 0 <= nc <= N-1:
#                         cur_sum += fly[nr][nc]
#             if cur_sum > max_t:
#                 max_t = cur_sum
#     # x
#     max_x = 0
#     for r in range(N):
#         for c in range(N):
#             cur_sum = fly[r][c]
#             for length in range(1, M):
#                 for dx, dy in [(1,-1), (-1,1), (-1,-1), (1,1)]:
#                     nr = r + dx*length
#                     nc = c + dy*length

#                     if 0<= nr <= N-1 and 0 <= nc <= N-1:
#                         cur_sum += fly[nr][nc]
#             if cur_sum > max_t:
#                 max_t = cur_sum

#     print(f"#{tc} {max(max_t, max_x)}")

# 파리퇴치

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())

#     fly = [list(map(int, input().split())) for _ in range(N)]
    
#     max_fly = 0
#     for r in range(N-M+1):
#         for c in range(N-M+1):
#             cur_sum = fly[r][c]
#             for width in range(M):
#                 for length in range(M):
#                     cur_sum += fly[r+width][c+length]
#             cur_sum -= fly[r][c]
#             if cur_sum > max_fly:
#                 max_fly = cur_sum
#     print(f"#{tc} {max_fly}")

# 전기버스
# T = int(input())
# for tc in range(1, T+1):
#     k, n, m = map(int, input().split())
#     station = list(map(int, input().split()))
#     station.append(n)

#     position = 0
#     count = 0
#     while position + k < n:
    
#         reachable = [i for i in station if position< i < position+k+1]
#         if not reachable:
#             count = 0
#             break           
#         position = max(reachable)
#         count += 1

#     print(f"#{tc} {count}")


arr = [42, 7, 19, 3, 56, 14, 28, 9]


# def bubble(arr):
#     for i in range(len(arr)-1,0,-1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# print(bubble(arr))

# def selection(arr):
#     for i in range(len(arr)-1):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[min_idx], arr[i] = arr[i], arr[min_idx]
#     return arr
# print(selection(arr))

def counting(arr, temp):
    count = [0] * (max(arr)+1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    
    for j in range(1, max(arr)+1):
        count[j] += count[j-1]
    for k in range(len(arr)-1, -1, -1):
        count[arr[k]] -= 1
        temp[count[arr[k]]] = arr[k]
    return temp
result = [0]*len(arr)

# print(counting(arr, result))

def binary(arr, key):
    start = 0
    end = len(arr)-1
    while start < end:
        middle = (start+end)//2

        if arr[middle] == key:
            return middle
        elif arr[middle] < key:
            start = middle
        elif arr[middle] > key:
            end = middle
    return -1
print(binary(counting(arr, result),42))