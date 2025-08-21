# 백준 1260번 DFS와 BFS

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
# 입력으로 주어지는 간선은 양방향  => *** 무방향 그래프다 *****

import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
# input() 보다 훨씬 빠르게 동작하여 시간 초과를 방지합니다.
input = sys.stdin.readline

# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
n, m, v = map(int, input().split())

# 인접 행렬 생성: (N+1) x (N+1) 크기의 2차원 리스트를 0으로 초기화
# 정점 번호를 인덱스로 바로 사용하기 위해 크기를 N+1로 설정합니다.
graph = [[0] * (n + 1) for _ in range(n + 1)]

# 간선 정보 입력받아 인접 행렬에 표시
for _ in range(m):
    a, b = map(int, input().split())
    # 무방향 그래프이므로 양쪽 모두 연결되었음을 표시
    graph[a][b] = graph[b][a] = 1

# 방문 기록을 위한 리스트 (DFS, BFS 각각 필요)
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

# --- 깊이 우선 탐색 (DFS) ---
# 재귀 함수를 이용해 구현
def dfs(start_node):
    # 1. 현재 노드를 방문 처리
    visited_dfs[start_node] = True
    print(start_node, end=' ')

    # 2. 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    # 문제 조건에 따라 정점 번호가 작은 것부터 방문해야 하므로 1번부터 N번까지 순서대로 확인
    for i in range(1, n + 1):
        # 연결되어 있고(graph[start_node][i] == 1) 아직 방문하지 않았다면(not visited_dfs[i])
        if graph[start_node][i] == 1 and not visited_dfs[i]:
            dfs(i) # 해당 노드를 시작으로 다시 DFS 수행

# --- 너비 우선 탐색 (BFS) ---
# 큐(Queue) 자료구조를 이용해 구현
def bfs(start_node):
    # 1. 시작 노드를 큐에 넣고 방문 처리
    # collections.deque는 양쪽에서 데이터를 넣고 빼는 속도가 빨라 큐로 사용하기에 효율적입니다.
    queue = deque([start_node])
    visited_bfs[start_node] = True

    # 2. 큐가 빌 때까지 반복
    while queue:
        # 큐에서 노드를 하나 꺼내옴 (가장 먼저 들어온 노드)
        current_node = queue.popleft()
        print(current_node, end=' ')

        # 3. 꺼낸 노드와 연결된 모든 인접 노드를 확인
        # 문제 조건에 따라 정점 번호가 작은 것부터 방문해야 하므로 1번부터 N번까지 순서대로 확인
        for i in range(1, n + 1):
            # 연결되어 있고(graph[current_node][i] == 1) 아직 방문하지 않았다면(not visited_bfs[i])
            if graph[current_node][i] == 1 and not visited_bfs[i]:
                # 해당 노드를 큐에 추가하고 방문 처리
                queue.append(i)
                visited_bfs[i] = True

# 함수 호출 및 결과 출력
dfs(v)
print() # 줄 바꿈
bfs(v)




###############################################################################################
###############################################################################################

import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
n, m, v = map(int, input().split())

# 인접 리스트 생성: 각 정점에 연결된 노드들을 담을 빈 리스트를 N+1개 생성
# graph[i]는 i번 노드와 연결된 노드들의 리스트가 됩니다.
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력받아 인접 리스트에 추가
for _ in range(m):
    a, b = map(int, input().split())
    # 무방향 그래프이므로 양쪽 모두에 추가
    graph[a].append(b)
    graph[b].append(a)

# *** 매우 중요한 부분 ***
# 문제 조건에서 "방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문"해야 함
# 따라서 각 정점에 연결된 노드 리스트를 오름차순으로 정렬해야 합니다.
for i in range(1, n + 1):
    graph[i].sort()

# 방문 기록을 위한 리스트 (DFS, BFS 각각 필요)
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

# --- 깊이 우선 탐색 (DFS) ---
# 재귀 함수를 이용해 구현
def dfs(start_node):
    # 1. 현재 노드를 방문 처리
    visited_dfs[start_node] = True
    print(start_node, end=' ')

    # 2. 현재 노드와 연결된(인접한) 다른 노드를 재귀적으로 방문
    # graph[start_node] 리스트에는 현재 노드와 연결된 노드들만 들어있습니다.
    # 위에서 정렬했기 때문에, for문을 순서대로 도는 것만으로 번호가 작은 순서대로 방문하게 됩니다.
    for adjacent_node in graph[start_node]:
        # 인접 노드가 아직 방문하지 않은 노드라면
        if not visited_dfs[adjacent_node]:
            dfs(adjacent_node) # 재귀 호출

# --- 너비 우선 탐색 (BFS) ---
# 큐(Queue) 자료구조를 이용해 구현
def bfs(start_node):
    # 1. 시작 노드를 큐에 넣고 방문 처리
    queue = deque([start_node])
    visited_bfs[start_node] = True

    # 2. 큐가 빌 때까지 반복
    while queue:
        # 큐에서 노드를 하나 꺼냄
        current_node = queue.popleft()
        print(current_node, end=' ')

        # 3. 꺼낸 노드와 연결된 모든 인접 노드를 확인
        # graph[current_node] 리스트를 순회하며 인접 노드를 탐색
        for adjacent_node in graph[current_node]:
            # 인접 노드가 아직 방문하지 않은 노드라면
            if not visited_bfs[adjacent_node]:
                # 해당 노드를 큐에 추가하고 방문 처리
                queue.append(adjacent_node)
                visited_bfs[adjacent_node] = True

# 함수 호출 및 결과 출력
dfs(v)
print() # 줄 바꿈
bfs(v)