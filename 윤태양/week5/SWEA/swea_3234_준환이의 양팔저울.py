t = int(input())

for tc in range(1, t+1):
    answer = 0

    n = int(input())
    weight = list(map(int, input().split()))

    dp = [{} for _ in range(2**9)]
    