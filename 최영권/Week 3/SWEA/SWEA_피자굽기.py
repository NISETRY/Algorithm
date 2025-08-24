from collections import deque

T = int(input())
for tc in range(1, T+1):
    q = deque()
    N, M = map(int, input().split())

    pizzas = list(map(int, input().split()))

    next_pizza = N
    oven = deque([0] * N)
    d = 0 
    
    while len(oven) != 1:
        oven.
            
    print(oven)
    