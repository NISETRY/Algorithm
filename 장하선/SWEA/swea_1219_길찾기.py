for tc in range(1,11):
    input()
    k=list(map(int, input().split()))
    route=[[] for _ in range(100)]
    visited=[False]*100
    for i in range(len(k)-1):
        if i%2==0:
            route[k[i]].append(k[i+1])
    stack=[0]
    visited[0]=True
    res=0

    while stack:
        loc=stack.pop()
        if loc==99:
            res=1
            break  
        for x in route[loc]:
            if not visited[x]:
                stack.append(x)
                visited[x]=True
    print(f'#{tc} {res}')