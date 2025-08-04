n = int(input())

graph = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
move = [[1,0],[-1,0],[0,1],[0,-1]]
cost = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        graph[i][j] =  temp[j]
                
def bfs(a,b):
    visited[a][b] = 1
    que = [[a,b]]
    cost1 = graph[a][b]
    
    while que:
        a, b = que.pop(0)
        
        for x,y in move:
            a = a+x ; b = b+y
            if 0<=a<n and 0<=b<n:
                if graph[a][b] !=0 and visited[a][b] == 1:
                    cost1 += graph[a][b]
                    return cost1
                
                elif graph[a][b] != 0 and visited[a][b] == 0:
                    cost1 += graph[a][b]
                    visited[a][b] = 1
                    que.append([a,b])
                 

for i in range(n):
    for j in range(n):
        cost.append(bfs(i,j))
        
print(cost)