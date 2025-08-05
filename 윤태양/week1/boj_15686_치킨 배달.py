import copy

n, m = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
chicken_num = 0
chicken_idx = [[-1,-1]]
for z in range(n):
    temp = list(map(int, input().split()))
    for x in range(n):
        graph[z][x] = temp[x]
        if temp[x] == 2:
            chicken_num+=1
            chicken_idx.append([z,x])
##### 인풋 ###########################################
com = []
com_chicken = []
def comb(count, idx):
    if count == m:
        com_chicken.append(com[:])
        return
    
    else:
        for i in range(1, chicken_num+1):
            if i > idx:
                com.append(i)
                comb(count+1, i)
                com.pop()            
comb(0,0)
##### 조합 ###########################################
move = [[-1,0],[1,0],[0,1],[0,-1]]

def bfs(a,b): #bfs a,b 조건 -> 집 이어야 함
    visited[a][b] = 1
    que = [[a,b]]
    while que:
        a, b = que.pop(0)    # 종료조건
        if new_graph[a][b] == 3:
            break
        
        for i, j in move:
            x,y = a+i, b+j
            if 0<=x<n and 0<=y<n:
                if visited[x][y] == 0:
                    que.append([x,y])
                    visited[x][y] = visited[a][b] + 1 # 마지막에 1 빼줘야 함(아마도)
                    
    return visited[a][b]
##### bfs ###########################################
for i in range(len(com_chicken)):
    com_chicken[i][0] = chicken_idx[com_chicken[i][0]]
    com_chicken[i][1] = chicken_idx[com_chicken[i][1]]
##### idx ###########################################
ans = []

for i in range(len(com_chicken)):
    c_idx = com_chicken[i]
    
    for j in range(len(c_idx)):
        new_graph = copy.deepcopy(graph)
        new_graph[c_idx[j][0]][c_idx[j][1]] = 3

for k in range(n):
    for l in range(n):
        if new_graph[k][l] == 1:
            visited = [[0 for _ in range(n)] for _ in range(n)]
            ans.append(bfs(k,l))

print(min(ans))
                