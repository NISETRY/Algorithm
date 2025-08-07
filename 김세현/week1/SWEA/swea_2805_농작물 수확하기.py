T = int(input())
 
for tc in range(T):
 
    N = int(input())
    l = 0
    k = []
    for i in range(N):
        l = input()   
        k.append(l)
    # print(k)
 
    result = []
    for i in range(N):
        a = N//2
        b = N//2 + 1
        d = list(k[i])
 
        if i <= N//2:
            c = d[a-i:b+i]
            result.append(c)
        elif i > N//2:
            c = d[i-a:2*a+b-i]
            result.append(c)
    # print(result)
 
    p = []
    for sub in result:
        for val in sub:
            p.append(int(val))
 
    print(f'#{tc+1} {sum(p)}')