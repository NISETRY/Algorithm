T = 10
 
def dfs(node):
    global answer
 
    if node == 99: # 도착 노드에 도달하려면
        answer = 1 # 답을 1로 설정
        return
     
    for next_node in adj_list[node]: # 현재 갈 수 있는 모든 노드에대해
 
        if visited[next_node]: # 이미 방문한 노드면 pass
            continue
 
        visited[next_node] = 1 # 방문 체크
        dfs(next_node) # 재귀 호출
        visited[next_node] = 0 # 다른 경로 탐색 위해 방문 해제
 
 
for tc in range(1, T+1):
    _, M = map(int, input().split())
    info = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)] # 인전 리스트 생성
    answer = 0
    visited = [0]*100
     
    for i in range(M):
        a = info[2*i]
        b = info[2*i+1]
 
        adj_list[a].append(b)
     
    visited[0] = 1
    dfs(0)
    visited[0] = 0
 
    print(f'#{tc} {answer}')