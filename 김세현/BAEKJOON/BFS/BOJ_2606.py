from collections import deque

N = int(input()) # 컴퓨터 개수
L = int(input()) # 연결선 개수

graph = [[] for _ in range(N+1)]
visited = [0] *(N+1) # 방문한 컴퓨터인지 표시
cnt = 0

for i in range(L):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    global cnt 
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)



