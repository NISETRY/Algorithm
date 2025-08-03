# 1차원 배열
from dask.array import average

# 10807번

# N = int(input())
# l = list(map(int, input().split()))
# v = int(input())
# print(l.count(v))
# 10871번
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
#
# for i in A:
#     if i<X:
#         print(i, end= ' ')
# 10818번

# N = int(input())
# lst = list(map(int, input().split()))
# print(min(lst), max(lst))

# 2562번
# nums = [int(input()) for _ in range(9)]
#
# print(max(nums))
# print(nums.index(max(nums))+1)


# 10810번
# N, M = map(int, input().split())
# basket = [0] * N
# for _ in range(M):
#     i, j, k = map(int, input().split())
#     for r in range(i-1, j):
#         basket[r] = k
# for ball in basket:
#     print(ball, end =' ')

# 10813번
# N, M = map(int, input().split())
# basket = [i for i in range(1,N+1)]
# for _ in range(M):
#     a, b =map(int, input().split())
#     basket[a-1], basket[b-1] = basket[b-1], basket[a-1]
#
# for bsk in basket:
#     print(bsk, end = ' ')



# 5597번
# students = [i for i in range(1,31)]
# for _ in range(28):
#     student = int(input())
#     students.remove(student)
# for stu in students:
#     print(stu)
# 3052번
# lst = []
# for i in range(10):
#     a = int(input())
#     if a % 42 not in lst:
#         lst.append(a % 42)
# print(len(lst))

# 10811번
# N, M = map(int, input().split())
# basket = [i for i in range(1,N+1)]
# for _ in range(M):
#     i, j = map(int, input().split())
#     basket[i-1:j] = basket[i-1:j][::-1]
# for bsk in basket:
#     print(bsk, end =' ')


# 1546번
# N = int(input())
# scores= list(map(int, input().split()))
# M = max(scores)
# sum = 0
# for score in scores:
#     sum += score
#
# print((sum/len(scores))/max(scores) * 100)