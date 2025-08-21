# 1번 코드
from collections import deque

T = 10

for tc in range(T):
    input()
    numbers = list(map(int, input().split()))
    queue = deque(numbers)

    decrease = 1

    while True:
        num = queue.popleft()  
        num -= decrease     

        # 0보다 작아지면 0으로 만들고 큐에 추가한 뒤 종료
        if num <= 0:
            queue.append(0)
            break
        else:
            queue.append(num)

        decrease += 1

        if decrease > 5:
            decrease = 1

    print(f"#{tc+1} {' '.join(map(str, queue))}")

# # 2번 코드
# from collections import deque

# T = 10

# for tc in range(1, T+1):
#     input()
#     q = deque(map(int, input().split()))

#     while True:

#         for i in range(1, 6):
#             a = q.popleft()
#             if a - i <= 0:
#                 q.append(0)
#                 break
#             q.append(a - i)

#         if q[-1] == 0:
#             break

#     print(f'#{tc}', *q)