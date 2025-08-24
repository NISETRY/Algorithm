from collections import deque
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 입력받은 M개의 피자
    pizzas = deque(map(int, input().split()))
    contrast_q = pizzas.copy()
    # 크기 N짜리 오븐
    oven = deque()
    origin_num = deque()
    # 오븐안에 일단 N개있을때까지는 피자 채우기
    # M개의 피자에서 가장 왼쪽 것 가져와서
    # 오븐에 오른쪽부터 밀어넣기
    # 기존 번호는 origin_num에 담아두기
    for j in range(N):
        tmp1 = pizzas.popleft() 
        oven.append(tmp1)
        origin_num.append(tmp1)
    while True:
        # 오븐 돌리기 전 번호를 담을 덱
        if oven.count(0) == N-1:
            for i in range(len(oven)):
                if oven[i] != 0:
                    answer = contrast_q.index(origin_num[i])+1
                    print(f"#{tc} {answer}")
            break
             
        # 오븐안에 갯수가 N개면
        # 가장 왼쪽 치즈양을 2로 나눈 몫만큼만 남기고 오른쪽으로 넣기
        # 원본 숫자도 같이 돌리기 -> 2개가 돌아가는 꼴, 시간이 2배로 걸리겠지
        elif len(oven) == N:
            left = oven.popleft()
            num = origin_num.popleft()
            left = left // 2
            if left == 0 and len(pizzas) > 0:
                tmp2 = pizzas.popleft() 
                oven.append(tmp2)
                origin_num.append(tmp2) 
            else:
                oven.append(left)
                origin_num.append(num)
                
                