t = int(input())

for tc in range(t):
    day, month, quarter, year = map(int, input().split())
    plan = list(map(int, input().split()))
    charge = year

    dp = [0]*13

    for i in range(1, 13):
        dp[i] = min(dp[i-1] + plan[i-1]*day, dp[i-1] + month)
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + quarter)

        if dp[i] >= charge:
            break

    else:
        charge = dp[12]

    print(f'#{tc+1} {charge}')


