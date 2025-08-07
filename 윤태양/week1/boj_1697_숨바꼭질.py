k, n = map(int, input().split())
visited = [0]*100001
graph = [0]*100001                 

def act(n):
    move1 = int(n/2)
    move2 = n+1
    move3 = n-1
    if n%2==0:
        return [move1,move2,move3]
    else:
        return [move2,move3]

def bfs(n):
    que = [n]
    visited[n] = 1
    cnt = 0

    while que:
        a = que.pop(0)
        move = act(a)

        for i in move:
            if i>=0 and i<=100000:
                if visited[i] == 0:
                    cnt+=1
                    visited[i] = 1
                    graph[i] = graph[a] + 1
                    que.append(i)  
    return graph[k]

if k>=n:
    print(k-n)
else:
    print(bfs(n))                            # 숨바꼭질 최적화 100ms
    

# from collections import deque
# k, n = map(int, input().split())
# visited = [0]*100001

# def act(n):
#     move1 = int(n/2)
#     move2 = n+1
#     move3 = n-1
#     if n%2==0:
#         return [move1,move2,move3]
#     else:
#         return [move2,move3]

# def bfs(n):
#     visited.append(n)
#     que = deque()
#     que.append([n])
#     visited[n] = 1

#     while True:    
#         a = que.popleft()
#         last = a[-1]
#         if last ==k:
#             return a
#         move = act(last)

#         for i in move:
#             if visited[i] == 0:  # O(1)
#                 visited[i] = 1 # O(1)
#                 temp = a.copy() # O(n)
#                 temp.append(i)  # O(1)
#                 que.append(temp)
# if k>=n:
#     print(k-n)
# else:
#     print(len(bfs(n))-1)   # 느린 숨바꼭질 2800ms
                                             