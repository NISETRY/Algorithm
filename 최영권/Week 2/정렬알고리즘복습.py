arr = [42, 7, 19, 3, 56, 14, 28, 9]

# 버블정렬
# def bubble_sort(arr):
#     for idx in range(len(arr)-1, 0, -1):
#         for j in range(idx):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# # print(bubble_sort(arr))

# # 선택정렬
# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
# # print(selection_sort(arr))


# # 카운팅 정렬
# def counting_sort(arr, temp, k):
#     # arr : 입력 배열
#     # temp : 정렬된 배열
#     # count : 카운트 배열
#     count = [0] * (k+1) # 충분한 공간 확보
#     for i in range(len(arr)):
#         count[arr[i]] += 1
    
#     for j in range(1, k+1):
#         count[j] += count[j-1]

#     for i in range(len(arr)-1, -1, -1):
#         count[arr[i]] -= 1
#         temp[count[arr[i]]] = arr[i]
    
# result = [0] * len(arr)
# counting_sort(arr, result, max(arr))
# print(result)

def bubble4(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble4(arr))


def selection(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
print(selection(arr))

def counting(arr, temp):

    count = [0] * (max(arr)+1)
    for i in range(len(arr)):
        count[arr[i]] += 1

    for j in range(1, max(arr)+1):
        count[j] += count[j-1]


    for i in range(len(arr)-1, -1, -1):
        count[arr[i]] -= 1               # 
        temp[count[arr[i]]] = arr[i]

result = [0] * len(arr)
counting(arr, result)
print(result)