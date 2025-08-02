# 27866번
# str = input()
# idx = int(input())
# print(str[idx-1])
# 2743번
# print(len(input()))

# 9086번
# T = int(input())
# for i in range(T):
#     str = input()
#     print(str[0]+str[-1])

# 11654번
# 문자에서 아스키코드 값 : ord
# 아스키코드에서 문자 : chr
# str = input()
# print(ord(str))

# 11720번
# N = int(input())
# str = input()
#
# sum = 0
# for i in str:
#     sum += int(i)
# print(sum)

# 10809번
# S = input()
# lst = []
# for i in range(ord('a'), ord('z')+1):
#     lst.append(chr(i))
#
# for i in S:
#     str

# 2675번
# T = int(input())
# for _ in range(T):
#     a, b = input().split()
#     for i in b:
#         print(i*int(a), end="")

# 1152번
# lst = input().lstrip().split()
# print(len(lst))


# 11718번
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break


# 10809번
# S = input()
#
# alpha_lst = [i for i in range(ord('a'), ord('z')+1)]
#
# for idx in range(len(alpha_lst)):
#     if chr(alpha_lst[idx]) in S:
#         alpha_lst[idx] = S.index(chr(alpha_lst[idx]))
#     else:
#         alpha_lst[idx] = -1
#
# for i in alpha_lst:
#     print(i, end = ' ')

# 2908번
# A, B = input().split()
# if A[:][::-1] > B[:][::-1]:
#     print(A[:][::-1])
# elif B[:][::-1] > A[:][::-1]:
#     print(B[:][::-1])

# 5622번
#
# S = input().upper()
#
# sum = 0
# for i in S:
#     if i == 'A' or i == 'B' or i == 'C':
#         sum += 3
#     elif i == 'D' or i == 'E' or i == 'F':
#         sum += 4
#     elif i == 'G' or i == 'H' or i == 'I':
#         sum += 5
#     elif i == 'J' or i == 'K' or i == 'L':
#         sum += 6
#     elif i == 'M' or i == 'N' or i == 'O':
#         sum += 7
#     elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
#         sum += 8
#     elif i == 'T' or i == 'U' or i == 'V':
#         sum += 9
#     elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
#         sum += 10
# print(sum)