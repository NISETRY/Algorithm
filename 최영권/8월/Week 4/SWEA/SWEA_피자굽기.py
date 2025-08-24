from collections import deque
T = int(input())

for tc in range(1, T+1):
    size, num_pizza = map(int, input().split())
    pizzas = deque(map(int, input().split()))
    oven = deque()
    nums = 0
    for i in range(size):
        nums += 1
        oven.append([pizzas.popleft(), nums])
    
    while len(oven) > 1:
        left, num = oven.popleft()
        left = left // 2
        if left != 0:
            oven.append([left, num])
        else:
            if len(pizzas) >= 1:
                nums += 1
                oven.append([pizzas.popleft(), nums])
    print(f"#{tc} {oven[0][1]}")
        