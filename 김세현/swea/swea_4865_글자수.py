T = int(input())

for tc in range(T):

    str1 = list(input().strip())
    str2 = list(input().strip())

    max_count = 0

    for ch in set(str1):
        count = 0
        for c in str2:
            if c == ch:
                count += 1
        if count > max_count:
            max_count = count

    print(f'#{tc+1} {max_count}')