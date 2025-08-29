import math
def dfs(count, left, right):
    global answer

    if left >= total_weight / 2:
        answer += 2**(N-count)*math.factorial(N-count)
        return
    
    if count == N:
        answer += 1
        return
    
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(count+1, left+weights[i], right)
        if right + weights <= left:
            dfs(count+1, left, right + weights[i])
        visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    answer = 0
    N = int(input())   # 무게추의 수

    weights = list(map(int, input().split()))
    total_weight = sum(weights)

    # 무게추 쓴 놈인지 안쓴놈인지
    visited = [0] * N

    dfs(0, 0, 0)