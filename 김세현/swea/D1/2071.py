T = int(input())

for tc in range(T):
    num = list(map(int, input().split()))

    result = round(sum(num)/len(num))

    print(f'#{tc+1} {result}')

