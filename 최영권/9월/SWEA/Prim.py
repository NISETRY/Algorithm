import sys
# import heapq
from heapq import heappush, heappop
sys.stdin = open("C:/Users/SSAFY/Desktop/Algorithm/최영권/9월/SWEA/input.txt", "r")


# 특정정점 기준으로 시작
# - 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 간다
# - 작은 노드를 먼저 꺼내기 위해 우선순위큐(heapq)를 활용한다
def prim(start_node):
    pq = [(0,start_node)] # -> pq : priority que, 0은 가중치, 왜 0을 앞에 뒀어? -> 우선순위 큐를 이용하기 위해서
    MST = [0] * V # visited와 동일하다
    min_weight = 0
      
    while pq:
        weight, node = heappop(pq)   # 가장 작은 가중치 
        # 이미 방문한 노드라면 continue
        if MST[node]:
            continue
        
        MST[node] = 1
        min_weight += weight
        
        
        for next_node in range(V):
            # 갈 수 없으면 continue
            if graph[node][next_node] == 0:
                continue
            
            # 이미 방문했으면 continue
            if MST[next_node]:
                continue
            
            # 원래 BFS에서는 여기서 방문처리 -> heapq에 넣기 전에 방문처리해버리면 최소를 구할 수 없음
            # 0 -> 1, 2 로 가서 21이 아니라 32가 더해짐
            
            heappush(pq, (graph[node][next_node], next_node))
        
    
    return min_weight

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]   # 인접행렬

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight  # 양방향
    
result = prim(0) # 출발정점과 함께 시작
# 출발 정점을 바꾸어도 출발정점은 같아야된다
# 하지만 그래프가 다르게 나올 수도 있다
print(f"최소 비용은:", result)