# 2739번
# num = int(input())
# for i in range(1,10):
#     print('{} * {} = {}'.format(num, i, num*i))

# 10950번
# test = int(input())
# for i in range(test):
#     a, b = map(int, input().split())
#     print(a+b)

# 8393번
# N = int(input())
# sum = 0
# for i in range(1, N+1):
#     sum += i
# print(sum)

# print(N*(N+1) //2)

# 25304번
# total_price = int(input())
# count_item = int(input())
# sum = 0
# for _ in range(count_item):
#     price, quantity = map(int, input().split())
#     sum += (price * quantity)
#
# if sum == total_price:
#     print("Yes")
# else:
#     print("No")


# 25314번
# N = int(input())
#
# repeat = N // 4
# print('long ' * repeat + 'int')

# 15552번
import sys

# test = int(sys.stdin.readline().rstrip())
# for i in range(test):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)

# 11021번
input = sys.stdin.readline
# test = int(input())
# for i in range(1, test+1):
#     a, b = map(int, input().split())
#     print("Case #{}: {}".format(i, a+b))

# 11022번
# test = int(input())
#
# for i in range(1, test+1):
#     a, b = map(int, input().split())
#     print("Case #{}: {} + {} = {}".format(i, a, b, a+b))

# 2438번
# test = int(input())
# # for i in range(1,test+1):
# #     print('*' * i)
#
# for i in range(1, test+1):
#     print(' ' * (test-i) + '*'*i)

# 2439번
# while True:
#     try:
#         a,b = map(int, input().split())
#         print(a+b)
#     except:
#         break
