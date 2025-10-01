from collections import deque

# input data
# 1 3
# 1 5
# 4 1
# 5 4
# 4 3
# 5 2
# 3 5
# 3 2
# 2 4
# 2 1

graph=[[] for _ in range(6)]
for i in range(10):
    n,m=map(int,input().split())
    graph[n].append(m)
que=deque([(1)])
visited=[1]
while que:
    x=que.popleft()
    for i in graph[x]:
        if i not in visited:    
            que.append(i)
            visited.append(i)
print(visited)