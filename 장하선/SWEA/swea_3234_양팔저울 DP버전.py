def dfs(cnt,diff):
    global visited

    # DP 확인
    if dp[visited].get(diff):
        return dp[visited][diff]

    # 탈출조건
    if cnt==n:
        dp[visited][diff]=1
        return dp[visited][diff]
    
    case_cnt=0
    for i in range(n):
        # 2**i면 방문 처리가 되었다는 뜻
        if visited & (1<<i):
            continue
        # 방문 안한 곳이면 방문처리를 해줘야함
        visited |= (1<<i)
        case_cnt += dfs(cnt+1, diff+w[i])
        if diff-w[i]>=0:
            case_cnt += dfs(cnt+1,diff-w[i])
        visited ^= (1<<i)

    # DP 기록
    dp[visited][diff] = case_cnt

    # 최종 출력
    return case_cnt

T=int(input())
for tc in range(1,T+1):
    ans = 0
    n=int(input())
    w = list(map(int,input().split()))
    dp=[{} for _ in range(2**n)]
    visited=0
    ans=dfs(0,0)