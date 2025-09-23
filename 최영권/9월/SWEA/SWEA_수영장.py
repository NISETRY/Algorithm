T = int(input())
for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())
    plans = list(map(int, input().split()))
    answer = 0

    dp = [0] * len(plans)
    dp[0] = min(day*plans[0], month)
    for i in range(1, len(plans)):
        base = plans[i] * day
        dp[i] = dp[i-1] + min(base, month)
        if i >= 2:
            dp[i] = min(dp[i], dp[i-3] + quarter)

    answer = min(dp[-1], year)
    print(f"#{tc} {answer}")