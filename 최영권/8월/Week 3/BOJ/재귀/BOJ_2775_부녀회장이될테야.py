import sys
maxK, maxN = 14, 14
dp = [[0] * (maxN+1) for _ in range(maxK+1)]
for n in range(1, maxN+1):
    dp[0][n] = n

for k in range(1, maxK+1):
    dp[k][1] = 1
    for n in range(2, maxN+1):
        dp[k][n] = dp[k][n-1] + dp[k-1][n]



N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    print(dp[k][n])