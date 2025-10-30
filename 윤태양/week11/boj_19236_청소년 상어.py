import copy

graph = []
move = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]  # 방향 정의
ans = 0

for _ in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = list(map(int, input().split()))
    graph.append([[a1, b1 - 1], [a2, b2 - 1], [a3, b3 - 1], [a4, b4 - 1]]) # 물고기 저장


def swap(graph, shark_pos): # 물고기 자리 바꾸기 로직
    for num in range(1, 17):
        found = False
        for r in range(4):
            for c in range(4):
                if num == graph[r][c][0]:  # 해당 번호의 물고기 찾기
                    found = True
                    is_swap = False
                    di = graph[r][c][1]
                    tri = 0
                    while not is_swap and tri < 8:
                        nr, nc = move[di]
                        nx, ny = r + nr, c + nc
                        if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != shark_pos and graph[nx][ny][0] != -1:
                            graph[r][c][1] = di  
                            graph[r][c], graph[nx][ny] = graph[nx][ny], graph[r][c]
                            is_swap = True
                        else:
                            di = (di + 1) % 8  
                            tri += 1
                if found:
                    break
            if found:
                break


def dfs(graph, x, y, point):  # 상어가 물고기 먹기 로직
    global ans

    if not (0 <= x < 4 and 0 <= y < 4):
        return
    if graph[x][y][0] <= 0:
        return

    graph = copy.deepcopy(graph) # deep_copy로 한 이유: dfs끼리 다른 graph를 쓰게 하려고
    fish_num, di = graph[x][y]   # point 구하기
    new_point = point + fish_num # new_point로 한 이유: 다음 dfs에 누적값을 전달하려고
    ans = max(ans, new_point) 
    graph[x][y][0] = 0  

    swap(graph, (x, y))  

    for step in range(1, 4): # 상어는 1,2,3칸 갈 수 있으므로 경우에 따라 dfs
        nx = x + move[di][0] * step 
        ny = y + move[di][1] * step
        if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny][0] > 0:
            dfs(graph, nx, ny, new_point)


dfs(graph, 0, 0, 0)
print(ans)
