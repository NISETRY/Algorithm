T = int(input())

for tc in range(T):
    a = list(map(int, input().split()))
    s = 0

    for i in range(10):
        if a[i] % 2 == 1:
            s += a[i]

    print(f'#{tc+1} {s}')