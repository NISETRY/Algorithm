#
def dfs(count, diff):
    global visited
    if dp[visited].get(diff):
        return dp[visited][diff]

    if count == N:
        dp[visited][diff] = 1
        # N개 고르고 나온 결과를 누적하여 리턴해야한다
        return dp[visited][diff]      
    case_count = 0
    for i in range(N):
        # i번째까지 미뤄라
        # 방문되었었다
        if visited & (1 << i):
            continue
        visited |= (1 << i)
        case_count += dfs(count+1, diff+weights[i])
        if diff-weights[i] >= 0:
            case_count += dfs(count+1, diff-weights[i])
        visited ^= (1 << i)

    dp[visited][diff] = case_count
    return dp[visited][diff]


T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    total_weight = sum(weights)
 
    answer = 0
 
    # (1 <= N <= 9 문제에서 주어짐)
    dp = [{} for _ in range(2**9)]
    visited = 0
 
    answer = dfs(0, 0)
 
    print(f"#{tc} {answer}")