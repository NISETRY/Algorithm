# DP 이용한 피보나치
# numbers = list(range(0, 11))
# dp = [0] * len(numbers)

# dp[0], dp[1] = 0, 1
# for i in range(2,len(numbers)):
#     dp[i] = dp[i-1] + dp[i-2]
# print(dp[-1])

T = int(input())
numbers = list(range(1,13))
picked = []
def comb(cnt, idx):
    global count
    if cnt<N and sum(picked) >= K:
        return
    
    if cnt == N and sum(picked) == K:
        count += 1
        return
    
    for i in range(idx, len(numbers)):
        picked.append(numbers[i])
        comb(cnt + 1, i + 1)
        picked.pop()



for tc in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    comb(0, 0)
    print(f"#{tc} {count}")



