from collections import deque

tc = int(input())

for _ in range(tc):
    n, m, k, a, b = map(int,input().split()) # 접수 창수의 개수, 정비 창구의 개수, 고객수, 지갑을 놔두고간 접수 a, b
    a_time = list(map(int, input().split())) # 접수창고가 고장을 접수하는 데 걸리는 시간
    b_time = list(map(int, input().split())) # 정비창고가 고장을 고치는 데 걸리는 시간
    k_time = list(map(int, input().split())) # 고객놈들이 들어오는 시간
    que = deque()
    count, time = 0, 0

    while count != k:
        
        for i in k_time:
            if i == time:
                que.append(k_time.pop(i))
                

        
