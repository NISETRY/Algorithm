# swea 3234번 준환이의 양팔 저울

# 메모이제이션
def dfs(count, diff):
    global visited

    if dp[visited].get(diff):
        return dp[visited][diff]

    if count == N:
        dp[visited][diff] = 1
        return dp[visited][diff]

    case_count = 0
    for i in range(N):
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
    answer = 0

    N = int(input())
    weights = list(map(int, input().split()))

    # 무게 추를 놓은 상태, l-r
    dp =[{} for _ in range(2**9)]
    visited = 0

    # 초기 시작
    answer = dfs(0, 0) # 놓은 게 없는 상태, 그러므로 차이도 없음
