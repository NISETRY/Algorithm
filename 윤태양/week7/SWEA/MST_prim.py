from heapq import heappop, heappush

def prim(start_node):
    pque = [(0, start_node)] # 가중치, 노드 -> 가중치를 앞에 쓰는 이유는 sort할 때 편하려고    
    visited = [0] * v 
    min_weight = 0

    while pque:
        weight, node = heappop(pque)

        if visited[node]:
            continue

        visited[node] = 1
        min_weight += weight

        for next in range(v):
            if graph[node][next] == 0:
                continue

            if visited[next]:
                continue

            heappush(pque, (graph[node][next], next)) 

    return min_weight

v, e = map(int, input().split())
graph = [[0]*v for _ in range(v)]

for _ in range(e):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight

result = prim(0)
print(f'최소 비용 : {result}')


# 특정 정점 기준으로 시작
# 갈 수 있는 노드들 중 가중치가 가장 작은 노드 부터 간다
# 가중치를 판단하기 위해 heapq 사용 


# 7 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51