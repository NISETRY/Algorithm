str = [list(input()) for _ in range(5)]

# 최대 길이 뽑기
max_length = 0
for lst in str:
    if len(lst) > max_length:
        max_length = len(lst)
 
# 6으로 맞추기
for str_lst in str:
    while len(str_lst) < max_length:
        str_lst.append(' ')

# 세로로 뽑기
ans = ''
for row in range(max_length):
    for col in range(5):
        ans += str[col][row].strip()

print(ans)

