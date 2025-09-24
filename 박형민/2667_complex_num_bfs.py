from pprint import pprint

N = int(input())

visited = [[0] * N for _ in range(N)]
arr = [0] * N

for x in range(N):
    arr[x] = list(map(int, list(input())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]      # 그래프에서 上下左右 탐색할 델타

pprint(arr)
pprint(visited)



def bfs(r, c):
    global node_cnt

    visited[r][c] = 1
    q = []
    q.append([r, c])
    node_cnt += 1

    while q:
        r, c = q.pop(0)

        for k in range(4):
            new_r = r + dr[k]  # 上下左右 순서로 탐색
            new_c = c + dc[k]

            if 0 <= new_r < N and 0 <= new_c < N:
                if arr[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                    visited[new_r][new_c] = 1
                    q.append([new_r, new_c])
                    node_cnt += 1


def dfs(r, c):
    global node_cnt

    node_cnt += 1               # dfs 함수가 실행되는 순간 집이 있다는 뜻이므로 시작과 동시에 집(dfs 트리 상에서는 각 노드) 추가
    visited[r][c] = 1           # 방문 처리

    for k in range(4):
        new_r = r + dr[k]       # 上下左右 순서로 탐색
        new_c = c + dc[k]

        if 0 <= new_r < N and 0 <= new_c < N:
            if arr[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                # 上下左右 델타 탐색 결과가 arr 의 index 를 벗어나는 경우를 미리 막기 위해 조건문을 걸어 index 內 제한
                # visited[new_r][new_c] = 1
                # Todo: ?여기서 방문 처리 안해도 아래 dfs 함수에서 어차피 new_r, new_c 처리하지 않나?
                dfs(new_r, new_c)
        else:
            continue

        

trees = []                # 각 단지의 집 갯수를 넣을 단지들(각각 dfs 에서의 트리들) 리스트 생성

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:   # 현재 좌표 위치가 1 이면서(집이 있으면서), 방문 후
            node_cnt = 0
            bfs(i, j)
            trees.append(node_cnt)
#
trees.sort()
print(len(trees))
print(*trees, sep="\n")