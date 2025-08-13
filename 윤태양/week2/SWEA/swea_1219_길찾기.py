
# def bfs(a):
#     visited[a] = 1
#     que = [a]

#     while que:
#         x = que.pop(0)
#         if x == 99:
#             break

#         for i in graph[x]:
#             if visited[i] == 0:
#                 que.append(i)
#                 visited[i] = 1

#     if x == 99:
#         return 1
#     else:
#         return 0
temp = []
def dfs(a):
    global ans
    if a == 99:
        ans = 1
        return

    for i in graph[a]:
        dfs(i)
           
    

for tc in range(10):
    t, line = map(int, input().split())
    lines = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visited = [0] * 100
    ans = 0
    
    for i in range(len(lines)):
        if i%2==0:
            temp = lines[i]
        else:
            graph[temp].append(lines[i])
    dfs(0)

    print(f'#{tc+1} {ans}')
    


    
