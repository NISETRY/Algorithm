n = int(input())
from collections import deque
target1, target2 = map(int, input().split())

m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    mom, son = map(int, input().split())
    graph[son].append(mom)
    graph[mom].append(son)
print(graph)
chonsu = 0
visited = [0] * (n+1)
def bfs(start, end):
    global chonsu
    q = deque([start])

    visited[start] = 1
    while q:
        chonsu += 1
        for _ in range(len(q)):
            check = q.popleft()
            for nxt in graph[check]:
                if end != nxt and visited[nxt] == 0:
                    visited[nxt] = 1
                    q.append(nxt)
                elif end == nxt:
                    return chonsu
    for _ in range(1, len(visited)+1):
        if visited[end] == 0:
            return -1
    
print(bfs(target1, target2))


# from collections import deque

# # N is number of people in family
# N = int(input())
# # a, b are two target's number who check edges
# a, b = map(int, input().split())

# # M is number of edges
# M = int(input())

# family = []
# for i in range(M):
#     x, y = map(int,input().split())
#     family.append([x,y])

# # print(f'N: {N}')
# # print(f'a,b: {a,b}')
# # print(f'M: {M}')
# # print(f'family: {family}')

# trees = [0 for _ in range(N+1)]

# # print(f'trees: {trees}')

# for i in family:
#     trees[i[1]] = i[0]

# # print(f'trees: {trees}')

# # write path
# x_line = []
# def find_edges(x):
#     route = deque()
#     if trees[x] == 0:
#         x_line.append(x)
#         return
#     else:
#         x_line.append(x)
#         route.append(trees[x])

#         nx_nd = route.popleft()
#         find_edges(nx_nd)

# # write path
# y_line = []
# def find_y_edges(x):
#     route = deque()
#     if trees[x] == 0:
#         y_line.append(x)
#         return
#     else:
#         y_line.append(x)
#         route.append(trees[x])

#         nx_nd = route.popleft()
#         find_y_edges(nx_nd)

# find_edges(a)
# find_y_edges(b)
# # print(f'x_line: {x_line}')
# # print(f'y_line: {y_line}')

# LUCA = []
# for i in range(1,len(x_line)+1):
#     if x_line[-i] in y_line:
#         k = x_line[-i]
#         LUCA.append(k)
        
# w = len(LUCA)

# if LUCA:
#     print(len(x_line)+len(y_line) - 2*w)
# else:
#     print(-1)