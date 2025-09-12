# # 3명의 친구 부분집합 찾기
# arr = ['O', 'X']
# name = ['MIN', 'CO', "TIM"]
# path = []

# def recur(cnt):
#     if cnt == 3:
#         print(*path)
#         return
#     # 재귀호출 파트
#     # - 부분집합에 포함되는 경우
#     path.append(arr[0])
#     recur(cnt+1)
#     path.pop()
#     # - 포함되지 않는 경우
#     path.append(arr[1])
#     recur(cnt+1)
#     path.pop()


# recur(0)
# 두 번째 선택에서는
# 'MIN'이라는 친구가 포함된 상태를 저장하면서 
# name = ['MIN', 'CO', "TIM"]
# path = []

# def recur(cnt, subset):
#     if cnt == 3:
#         print(*subset)
#         return
    
#     # 포함시키는 경우
#     recur(cnt+1, subset + [name[cnt]])
#     # 포함시키지 않는 경우
#     recur(cnt+1, subset)  

# recur(0, [])

arr = ['A','B','C']
n = len(arr)

# # i : 0~2^n == i번째 부분집합
# def get_sub(tar):
#     for i in range(n):
#         if tar & 0x1:
#             print(arr[i], end = '')
#         tar >>= 1
# get_sub(6)
# print()
# print(1 << len(arr))
def get_sub(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end='')
        tar >>= 1

for target in range(1<<n):
    get_sub(target)
    print()
