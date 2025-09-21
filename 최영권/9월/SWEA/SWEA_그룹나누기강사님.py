# # DFS
# T = int(input())

# def dfs(node):
#     for next in adj_lst[node]: 
#         if visited[next]:
#             continue
#         visited[next] = 1
#         dfs(next)

# for tc in range(1, T+1):    
#     answer = 0
#     N, M  = map(int,input().split())
#     connections = list(map(int, input().split()))
#     adj_lst = [[] for _ in range(N+1)]
#     visited = [0] * (N+1)
#     for i in range(M):
#         idx1 = i*2
#         idx2 = idx1+1
        
#         adj_lst[connections[idx1]].append(idx2)
#         adj_lst[connections[idx2]].append(idx1)
    
#     for node in range(1, N+1):
#         if visited[node]:
#             continue
#         visited[node] = 1
#         answer += 1
#         dfs(node)
    
#     print(f"#{tc} {answer}")
    
    
# Union Find    
