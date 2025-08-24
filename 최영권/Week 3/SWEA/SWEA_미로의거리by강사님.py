from collections import deque
T = int(input())
dr = [-1,1,0,0]
dc = [0,0,1,-1]
for tc in range(1, T+1):
    N = int(input())
    graph = []
    answer = -1
    # 입력 + 시작점 찾기
    s_r, s_c = -1, -1
    for r in range(N):
        temp = list(map(int, input()))
        for c in range(N):
            if temp[c] == 2:
                s_r, s_c = r, c
        graph.append(temp)

    # BFS로 찾기 -> 최단경로를 찾기위해
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((s_r, s_c))   # 시작점은 변할 이유가 없음 그냥 참조만 하면됨
    visited[s_r][s_c] = 1

    flag = False     # 3을 찾으면 더이상 돌 필요없어서 True 해주고 반복문 탈출
    while q:         # q가 빌 때까지 돌아라
        
        answer += 1  # 현재 q의 길이는 

        for _ in range(len(q)):
            r, c = q.popleft()
            
            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]
                
                # 맵 안쪽이어야한다
                # 1이 아니어야한다
                # 방문 안했어야한다(visited)

                # 동치조건, 이중 하나라도 만족하면 다음 방향을 봐
                # 맵 바깥쪽이거나
                # 1이거나
                # 방문했거나
                if nr < 0 or nr >= N or nc < 0 or nc >= N or graph[nr][nc]==1 or visited[nr][nc]:
                    continue
                
                # 방문해볼만한 곳만 걸러준다
                if graph[nr][nc] == 3:
                    flag = True
                    break
                visited[nr][nc] = 1
                q.append((nr, nc))
            if flag:
                break
        if flag:
            break
       
    
    if not flag:
        answer = 0
    print(f"#{tc} {answer}")
    