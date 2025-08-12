t = int(input())
 
for tc in range(t):
    n, m = map(int, input().split())
    graph = [list(input()) for _ in range(n)]
    new_graph = [[0]*n for _ in range(n)]
    ans = ''
     
    for i in range(n):
        for j in range(n):
            new_graph[j][i] = graph[i][j]            # graph i/j swap
 
    for i in range(n):                               # i->j 순회하면서 회문 찾기
        for j in range(n):
            if j+m <=n:
                temp = graph[i][j:j+m]
                if temp == temp[::-1]:
                    ans = temp
 
    for i in range(n):                               # j->i 순회하면서 회문 찾기
            for j in range(n):
                if j+m <=n:
                    temp = new_graph[i][j:j+m]
                    if temp == temp[::-1]:
                        ans = temp
 
    print(f'#{tc+1} ', *ans, sep='')