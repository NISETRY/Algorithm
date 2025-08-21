# def solution(arr):
#     answer = []
#     for num in arr:
#         if not answer or answer[-1] != num:
#             answer.append(num)
#     return answer

'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''

def bfs(s, V):
    # 초기화
    visited = [0] * (V + 1) # visited 생성, 방문 기록용 리스트
    q = [s] # 큐 생성 (시작점을 넣음)
            # 시작점 인큐
    visited[s] = 1 # 시작점 인큐표시
    # 반복
    while q: # 탐색할 정점이 남아 있으면 (큐가 비어있지 않으면 반복)
        t = q.pop(0) # 디큐 (큐에서 하나 꺼냄)
        print(t) # visit(), 방문정점 출력

        for w in adj_lst[t]: # t에 인접한 모든 정점 w에 대해
            if visited[w] == 0: # 아직 방문 안 했다면
                q.append(w) # 큐에 추가
                visited[w] = visited[t] + 1 # 방문 표시 + 거리 기록
                # 인접하고 미방문인 정점 인큐, 인큐표시
    

V, E = map(int, input().split()) # 마지막 정점, 간선 수
arr = list(map(int, input().split()))

# 인접리스트
adj_lst = [[] for _ in range(V+1)] # V번행까지 준비
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1) # 방향표시가 없는 경우
    
bfs(1, V) # 1을 출발점으로 해서 V번까지 탐색 해보자



# for i in range(0, E*2, 2):
#     v1, v2 = arr[i], arr[i+1]

