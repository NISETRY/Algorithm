from collections import deque

T = int(input())

# 첫번째 위치인 거를 하나씩 확인해서 2로 나누기,
# 1이 될 때까지?

for tc in range(1, T+1):
    N, M = int(input().split())
    Ci = deque(map(int, input().split())) # 치즈 양

    while True:

        if all(0 for c in Ci):
            break
        for i in range(1, 6):
            a = q.popleft()
            if a - i <= 0:
                q.append(0)
                break
            q.append(a - i)

        if q[-1] == 0:
            break

    print(f'#{tc}', *q)
