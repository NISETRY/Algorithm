import copy

graph = []
move = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]  # 방향 정의
ans = 0

for _ in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = list(map(int, input().split()))
    graph.append([[a1, b1 - 1], [a2, b2 - 1], [a3, b3 - 1], [a4, b4 - 1]])


def swap(graph, shark_pos):
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


def dfs(graph, x, y, point):
    global ans

    if not (0 <= x < 4 and 0 <= y < 4):
        return
    if graph[x][y][0] <= 0:
        return

    graph = copy.deepcopy(graph)
    fish_num, di = graph[x][y]  
    new_point = point + fish_num
    ans = max(ans, new_point)
    graph[x][y][0] = 0  

    swap(graph, (x, y))  

    for step in range(1, 4):
        nx = x + move[di][0] * step
        ny = y + move[di][1] * step
        if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny][0] > 0:
            dfs(graph, nx, ny, new_point)


dfs(graph, 0, 0, 0)
print(ans)
