def comb(count, idx):
    global answer 

    if sum(temp) >= h:
        answer = min(sum(temp), answer)
        return
    
    if sum(temp) >= answer:
        return
    
    if count == n:
        return
    
    for i in range(n):
        if i > idx:
            temp.append(people[i])
            comb(count+1, i)
            temp.pop()


t = int(input())

for tc in range(t):
    n, h = map(int, input().split())
    people = list(map(int, input().split()))

    answer = 999999
    temp = []
    comb(0,-1)
    print(f'#{tc+1} {answer-h}')