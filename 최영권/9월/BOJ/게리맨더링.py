from itertools import combinations
from collections import deque

N = int(input())
population = [0] + list(map(int, input().split()))  # 인구 (1-indexed)
graph = [[] for _ in range(N+1)]

# 그래프 입력
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for v in data[1:]:
        graph[i].append(v)

# 연결 여부 확인 함수
def is_connected(group):
    q = deque([group[0]])
    visited = set([group[0]])
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if nxt in group and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return len(visited) == len(group)

answer = float('inf')

# 그룹 나누기
for r in range(1, N//2 + 1):  # 반까지만 하면 됨
    for comb in combinations(range(1, N+1), r):
        A = list(comb)
        B = [i for i in range(1, N+1) if i not in A]

        if is_connected(A) and is_connected(B):
            popA = sum(population[i] for i in A)
            popB = sum(population[i] for i in B)
            answer = min(answer, abs(popA - popB))
    
print(answer if answer != float('inf') else -1)