import pprint

t = int(input())

for tc in range(t):
    m, bc = map(int, input().split())
    
    user_a = list(map(int, input().split()))
    user_b = list(map(int, input().split()))
    ap = [list(map(int, input().split())) for _ in range(bc)]

    graph = [[[] for _ in range(11)] for _ in range(11)]
    move = [(0,-1),(1,0),(0,1),(-1,0)]

    for r,c,dis,charge in ap:
        for i in range(1, 11):
            for j in range(1, 11):
                if dis >= abs(r-i) + abs(c-j):
                        graph[j][i].append(charge)

    user_ab = [(0,0)]
    for i in range(m):
        a,b = user_a[i], user_b[i]
        user_ab.append((a,b))

    answer = 0
    a_now, b_now = (0,0), (10,10)
    charged_bc = [0]*bc

    for a,b in user_ab:
        a_now += move[a]
        b_now += move[b]

        if a_now == b_now:
            pass
            
    
    # 사용자 돌면서 조건문으로 맥스 충전량 계산