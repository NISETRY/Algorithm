'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''
def bfs(s, V):
    # 초기화
    visited = [0] * (V+1)    # visited 생성
    queue = [s]    # 큐 생성
    
    # 시작점 인큐
    visited[s] = 1    # 시작점 방문표시
        
    # 반복
    while queue:         # 탐색할 정점이 남아있으면
        t = queue.pop(0) # 디큐
        print(t)         # visit(), 방문정점 출력

        # 인접하고 미방문인 정점 인큐, 인큐표시
        for w in adj_lst[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1




V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adj_lst = [[] for _ in range(V+1)] # V번행까지 준비
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1)

# 이렇게도 만들 수 있다
# for i in range(0, E*2, 2):
#     v1, v2 = arr[i], arr[i+1]
    
bfs(1, V)

# 1에서 각 정점까지 최소거리의 합은?