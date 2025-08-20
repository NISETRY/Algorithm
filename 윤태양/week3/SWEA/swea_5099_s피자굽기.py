from collections import deque

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    pizza = deque(map(int, input().split()))

    idx_pizza = []
    for i in range(1, len(pizza)+1):     # 피자랑 IDX 같이 관리
        idx_pizza.append([i,pizza[i-1]])
    hwa = idx_pizza[:n]

    while True:
        if len(hwa) == 1:
            print(f'#{tc+1} {hwa[0][0]}')
            break

        if hwa[0][1] // 2 == 0:
            hwa.pop(0)
            try:
                hwa.append(idx_pizza[n])
                n += 1
            except:
                pass

        elif hwa[0][1] // 2 != 0:
            hwa[0][1] = hwa[0][1] // 2 
            temp = hwa.pop(0)
            hwa.append(temp)
            
