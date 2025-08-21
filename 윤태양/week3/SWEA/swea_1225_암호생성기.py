from collections import deque

for tc in range(10):
    input()
    que = deque(map(int, input().split()))
    cnt = 1

    while True:
        temp = que.popleft()   
        temp -= cnt
        cnt = cnt % 5 + 1 
        if temp <= 0:
            temp = 0
            que.append(temp)
            break
        else:
            que.append(temp)

    print(f'#{tc+1}', *que)