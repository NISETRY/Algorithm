T = int(input())

for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    count = [0] * len(str1)
    for i in range(len(str1)):
            if str1[i] in str2:
                  count[i] += str2.count(str1[i])
    print(f"#{tc} {max(count)}")