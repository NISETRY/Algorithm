from collections import deque
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
S, T = map(int, input().split())

# Please write your code here.
# 방문 가능한 정점을 담을 list 선언
ans=[]
visited=[0]*(n+1)

# 인접 리스트 생성
nearby=[[] for _ in range(n+1)]
for i in range(m):
    nearby[edges[i][0]].append(edges[i][1])

# 출근길에 방문 불가능한 정점들을 확인
queue=deque([S])
visited[S]=1
while queue:
    tmp=queue.popleft()
    cand=nearby[tmp]
    for i in cand:
        if not visited[i]:
            visited[i]=1
            if i!=T:
                queue.append(i)

# 퇴근길에는 출근길에는 방문 못 한 정점은 제외하고 방문하기
queue=deque([T])
while queue:
    tmp=queue.popleft()
    for u,v in edges:
        if v==tmp and visited[u]==1:
            visited[u]=2
            if u!=S:
                queue.append(u)
visited[S], visited[T]=0,0
print(visited)
# print(len(ans))