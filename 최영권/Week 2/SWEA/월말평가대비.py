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


# arr = [42, 7, 19, 3, 56, 14, 28, 9]


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

# def counting(arr, temp):
#     count = [0] * (max(arr)+1)
#     for i in range(len(arr)):
#         count[arr[i]] += 1
    
#     for j in range(1, max(arr)+1):
#         count[j] += count[j-1]
#     for k in range(len(arr)-1, -1, -1):
#         count[arr[k]] -= 1
#         temp[count[arr[k]]] = arr[k]
#     return temp
# result = [0]*len(arr)

# print(counting(arr, result))

# def binary(arr, key):
#     start = 0
#     end = len(arr)-1
#     while start < end:
#         middle = (start+end)//2

#         if arr[middle] == key:
#             return middle
#         elif arr[middle] < key:
#             start = middle
#         elif arr[middle] > key:
#             end = middle
#     return -1
# print(binary(counting(arr, result),42))

# 중복순열

# M = 2
# def perm(count):
    # if count == M:
    #     print(picked)
    #     return
    # for num in numbers:
    #     picked.append(num)
    #     perm(count+1)
    #     picked.pop()
# perm(0)

# 순열
# numbers = [1,2,3,4]
# picked = []
# numbers = [1,2,3,4,5]
# picked = []
# visited = [0] *len(numbers)
# M = 3
# def perm2(count):
#     if count == M:
#         print(picked)
#         return
#     for idx in range(len(numbers)):
#         if visited[idx] == 1:
#             continue
#         picked.append(numbers[idx])
#         visited[idx] = 1
#         perm2(count+1)
#         picked.pop()
#         visited[idx] = 0
# perm2(0)

# 조합
# def comb(count, idx):
#     if count == M:
#         print(picked)
#         return
#     for idx in range(idx, len(numbers)):
#         picked.append(numbers[idx])
#         idx += 1
#         comb(count+1, idx)
#         picked.pop()
#         idx -= 1
# # comb(0, 0)

# def comb2(count, idx):
#     if count == M:
#         print(picked)
#         return
#     for i in range(idx, len(numbers)):
#         picked.append(numbers[i])
#         comb2(count+1, i)
#         picked.pop()
        
# # comb2(0,0)

# # bubble
# # arr = [42, 7, 19, 3, 56, 14, 28, 9]

# def bubble(arr):
#     for i in range(len(arr)-1, 0,-1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
# # print(bubble(arr))

# def selection(arr):
#     for i in range(len(arr)-1):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[min_idx], arr[i] = arr[i], arr[min_idx]
#     return arr
# # print(selection(arr))

# def counting(arr, temp):
    # count = [0] * (max(arr)+1)  
    # for i in range(len(arr)):
    #     count[arr[i]] += 1

    # for j in range(1, max(arr)+1):
    #     count[j] += count[j-1]

    # for k in range(len(arr)-1, -1, -1):
    #     count[arr[k]] -= 1
    #     temp[count[arr[k]]] = arr[k]

    # return temp
# result = [0] * len(arr)
# print(counting(arr, result))

## 이진탐색
# arr = [3, 5, 7, 9, 12, 15, 18, 21, 25, 28, 31, 36, 40, 45, 50, 57, 63, 70, 78, 85]

# def binary(arr, key):
#     start = 0
#     end = len(arr)-1
    
#     while start < end:
#         middle = (start+end) // 2
#         if arr[middle] == key:
#             return middle
#         elif arr[middle] < key:
#             start = middle
#         elif arr[middle] > key:
#             end = middle
#     return -1
# print(binary(arr, 63))

## 달팽이

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     snail = [[0]* N for _ in range(N)]

#     time = []
#     for t in range(N):
#         time.append(N-t)
#         time.append(N-t)
#     time.remove(N)

#     dy = [0,1,0,-1]
#     dx = [1,0,-1,0]
#     num = 1
#     dir = 0
#     x, y = -1,0
#     for t in time:
#         for _ in range(t):
#             x += dx[dir]
#             y += dy[dir]
#             snail[y][x] = num
#             num += 1
#         dir = (dir+1)%4
        

#     for x in snail:
#         print(*x)
arr = [42, 7, 19, 3, 56, 14, 28, 9]
# def bubble(arr):
#     for i in range(len(arr)-1,-1,-1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# print(bubble(arr))

# def selection(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         arr[min_idx], arr[i] = arr[i], arr[min_idx]
#     return arr
# print(selection(arr))

# def counting(arr, tmp):

#     count = [0]*(max(arr)+1)

#     for i in range(len(arr)):
#         count[arr[i]] += 1

#     for j in range(1, max(arr)+1):
#         count[j] += count[j-1]

#     for k in range(len(arr)-1,-1,-1):
#         count[arr[k]] -= 1
#         tmp[count[arr[k]]] = arr[k]
#     return tmp
# result = [0] * len(arr)
# print(counting(arr, result))

# def binary(arr, key):
#     end = len(arr)-1
#     start = 0
#     while start <= end:
#         middle = (start+end) //2 
#         if arr[middle] == key:
#             return middle
#         elif arr[middle] > key:
#             end = middle
#         elif arr[middle] < key:
#             start = middle
#         return -1
# print(binary(counting(arr, result), 14))

# 회문

# T = int(input())
# for tc in range(1, T+1):
#     n, m = map(int, input().split())

#     lst = [list(input()) for _ in range(n)]
#     answer = ''
#     for r in lst:
#         for c in zip(*r):
            
#             for i in range(n-m+1):
#                 string = r[i:i+m]
#                 if string == string[::-1]:
#                     answer = string

    
#     for col in zip(*lst):
#         for j in range(n-m+1):
#             string = col[j:j+m]
#             if string == string[::-1]:
#                 answer= string

#     print(f"#{tc}", *answer, end='\n')

arr2 = [2, 5, 3, 0, 2, 3, 0, 3]
def counting_sort(arr, tmp):
    count = [0]*(max(arr)+1)

    # count : arr의 값 카운팅
    for i in range(len(arr)):
        count[arr[i]] += 1
    
    # count의 값을 누적합 -> count의 인덱스는 0~max(arr) -> j-1의 인덱스 에러를 방지하기 위해 1 ~ max(arr)까지 순회
    for j in range(1, max(arr)+1):
        count[j] += count[j-1]

    # 마지막 단계 arr배열을 정렬해줄 차례
    # arr의 마지막 값부터 정렬 -> 안정정렬
    # 마지막 값(3)을 가져와서 3의 누적 카운팅 값을 참조
    # 정렬할 리스트에 [참조한 값 - 1] 인덱스에 정렬할 값(3)을 넣고 
    # 누적 카운팅 값 -1
    for k in range(len(arr)-1, -1 ,-1):
        # tmp[count[3]] => tmp[7] = 3
        count[arr[k]] -= 1
        tmp[count[arr[k]]] = arr[k] 
        
    return tmp
result = [0] * len(arr2)
print(counting_sort(arr2, result))