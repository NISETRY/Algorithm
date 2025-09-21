def dfs(count, diff):
    global bit_mask

    if count == n:
        visited[bit_mask][diff] = 1
        return 1 # 상위 호출에 더해줄 값 / n층이면 무조건 1

    if visited[bit_mask].get(diff):
        return visited[bit_mask][diff] # 상위 호출에 더해줄 값 2 / n층이 아니라 1은 아님 

    counting = 0 # 상위 호출 counting 초기화

    for i in range(n):
        if not bit_mask & (1 << i):

            bit_mask |= (1 << i)
            counting += dfs(count+1, diff+weight[i]) # 왼 / 카운팅 누적

            if diff - weight[i] >= 0:
                bit_mask |= (1 << i)
                counting += dfs(count+1, diff-weight[i]) # 오 / 카운팅 누적

            bit_mask ^= (1 << i)

    visited[bit_mask][diff] = counting # 처음 계산한 새로운 상태
    return counting # dfs(0,0)의 값은 모든 카운팅이 더해졌을 때

t = int(input())

for tc in range(t):
    n = int(input())
    weight = list(map(int, input().split()))
    bit_mask = 0
    visited = [{} for _ in range(2**n)] # n개만 만들어도 됨

    answer = dfs(0,0)
    print(f'#{tc+1} {answer}')


