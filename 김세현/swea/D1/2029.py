T = int(input())

for tc in range(T):
    a, b = map(int, input().split())
    mok = a//b
    nam = a%b
    print(f'#{tc+1} {mok} {nam}')