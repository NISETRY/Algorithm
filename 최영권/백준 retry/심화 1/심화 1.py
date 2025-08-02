# 심화 1
# 25083번
# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \. \". L_r'")
# print("   `~\/")
# print("      |")
# print("      |")

# 3003번
# white_piece = [1, 1, 2, 2, 2, 8]
#
# input_piece = list(map(int, input().split()))
#
# for i in range(len(white_piece)):
#     print(white_piece[i] - input_piece[i], end = ' ')

# 2444번
#
# N = int(input())
# for i in range(1, N+1):
#     print(' ' * (N-i) + '*' * (2*i-1))
#     if i == N:
#         for j in range(N-1, 0, -1):
#             print(' ' * (N-j) + '*' * (2*j-1))

# 10988번
# s = input()
# if s == s[:][::-1]:
#     print(1)
# else:
#     print(0)

# 25206번
# grade = {'A+' : 4.5, 'A0' : 4, 'B+' : 3.5, 'B0' : 3, 'C+' : 2.5, 'C0' : 2, 'D+' : 1.5, 'D0' : 1, 'F' : 0, "P" : 0}
# count_lev = 0
# sum = 0
# for _ in range(20):
#     sub, level, grd = input().split()
#     count_lev += float(level)
#     sum += float(level) * grade.get(grd)
#     if grd == 'P':
#         count_lev -= float(level)
#
# print(f'{sum / count_lev:.6f}')


# 1157번
# s = list(input().upper()) # zZa
# alpha_count = [0] * 26
#
# for ch in s:
#     alpha_count[ord(ch) - ord('A')] += 1
#
# max_count = max(alpha_count)
# if alpha_count.count(max_count) > 1:
#     print('?')
# else:
#     print(chr(alpha_count.index(max_count) + ord('A')))

# 1316번
N = int(input())
count = 0

for _ in range(N):
    word = input()
    is_group_word = True
    seen = set()
    prev_char = ''

    for char in word:
        if char != prev_char:
            if char in seen :
                is_group_word = False
                break
            seen.add(char)
        prev_char = char

    if is_group_word:
        count += 1

print(count)

# 2941번
# alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# croatian = ['č', 'ć', 'dž', 'đ', 'lj', 'nj', 'š', 'ž']
#
# s = input()
#
# crotian_len = 0
# for i in range(len(s)):
