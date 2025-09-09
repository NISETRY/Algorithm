def dfs(count, money):
    global answer 
    if count == swap:    
        tmp = ''
        for i in money:
            tmp += str(i)
        answer = max(int(tmp), answer)        
        return     

    now = tuple(money)
    if now in visited[count]:
        return
    visited[count].add(now)


    for i in range(len(money)):
        for j in range(i+1, len(money)):
            money[i],money[j] = money[j],money[i]
            dfs(count+1, money)
            money[i],money[j] = money[j],money[i]

t = int(input())

for tc in range(t):
    temp, swap = input().split()
    money = list(map(int, temp)) ; swap = int(swap)
    pick = []
    visited = [set() for _ in range(swap+1)]
    answer = 0

    dfs(0,money=money)


    print(f'#{tc+1} {answer}')
