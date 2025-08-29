from collections import deque
N, M = map(int, input().split())


# 인접리스트 생성
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
# 1,2,3,4,5
# 자기에서 시작해서 N까지 모든 숫자를 방문할 때 걸리는 거리의 합을 구해야된다
# 순서
for num in range(1, N+1):
    nums_cnt = 0
    min_count = 0
    
    # 방문하고자 하는 숫자
    for i in range(1, N+1):
        q = deque([num])
        visited = [0] * (N+1)
        visited[num] = 1
        # 자기는 방문할 필요X
        if i == num:
            pass
        else:
            while q:
                start = q.popleft()
                for j in graph[start]:
                    if j == i:
                        min_count = min(min_count, nums_cnt)
                    else:
                        visited[j] = 1
                        q.append(j)
                nums_cnt += 1
                print('num :', num, 'cnt :', nums_cnt)