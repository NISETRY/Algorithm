t = int(input())
 
move = [[0,1], [1,0],[0,-1],[-1,0]] # 우하좌상 
def swap():
    global now
    if now == 3:
        now = 0
    else:
        now+=1
 
for tc in range(t):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    time = [0]*(2*n-1)
     
    l = n ; k = 1
    for i in range(len(time)):
        time[i] = l
        k = k -1
        if k == 0:
            k = 2 ; l -= 1
             
    v = 0
    now = 0  
    next_i = 0
    next_j = -1
    for i in time:
        if i != n:
            swap()
        for j in range(i):
            v += 1  
            next_i = next_i + move[now][0]
            next_j = next_j + move[now][1]  
            graph[next_i][next_j] = v
             
    print(f'#{tc+1}')                 
    for i in range(len(graph)):
        print(*graph[i])