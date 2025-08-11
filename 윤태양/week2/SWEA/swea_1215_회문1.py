for tc in range(10):
 
    length = int(input())
    graph = [list(input()) for _ in range(8)]
    new_graph = [[0]*8 for _ in range(8)]
    cnt = 0
     
    for i in range(8):
        for j in range(8):
            new_graph[j][i] = graph[i][j]
 
    for i in range(8):
        for j in range(8-length+1):
            temp = graph[i][j:j+length]
            if temp == temp[::-1]:
                cnt+=1
 
    for i in range(8):
        for j in range(8-length+1):
            temp = new_graph[i][j:j+length]
            if temp == temp[::-1]:
                cnt+=1
 
    print(f'#{tc+1} {cnt}')