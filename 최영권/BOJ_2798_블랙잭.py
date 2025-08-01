# N과 M을 받아 
# N개의 카드를 뽑아 합이 M과 가장 근접한 카드 3장의 합을 출력한다.


# N과 M을 받아 N개의 카드를 뽑는다.
N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 카드 3장을 뽑아 그 값을 M과 비교하여 값을 출력
choose3 = []
max_val = 0 

for i in range(-1, -len(nums), -1):
    second_nums = nums.pop(i)
    i += 1
    print(i, nums)
#     for num2 in second_nums:
#         third_nums = second_nums.pop(second_nums.index(num2))
#         for num3 in third_nums:
#             choose3.append(num1)
#             choose3.append(num2)
#             choose3.append(num3)

# print(choose3)