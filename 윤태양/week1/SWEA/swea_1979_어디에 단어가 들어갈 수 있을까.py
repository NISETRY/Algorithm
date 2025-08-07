t = int(input())
 
for tc in range(t):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
 
    for i in range(n):
        seri = 0
        for j in range(n):
            if graph[i][j] == 0:
                if seri == k:
                    cnt+=1
                seri = 0
            elif graph[i][j] == 1:
                seri +=1
 
        if seri == k:
            cnt+=1
 
    for j in range(n):
        seri = 0
        for i in range(n):
            if graph[i][j] == 0:
                if seri == k:
                    cnt+=1
                seri = 0
            elif graph[i][j] == 1:
                seri +=1
        if seri == k:
            cnt+=1
         
    print(f'#{tc+1} {cnt}')