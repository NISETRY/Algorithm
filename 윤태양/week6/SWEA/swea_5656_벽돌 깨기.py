from collections import deque
from pprint import pprint
from copy import deepcopy

def dfs(count):
    global answer, graph

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] != 0:
                cnt += 1
    answer = min(cnt, answer)

    if answer == 0:
        return

    if count == n:
        return 

    for r in range(h):
        for c in range(w):
            if graph[r][c] !=0 and (r ==0 or graph[r-1][c] == 0):
                og_graph = deepcopy(graph)
                block_break(r,c)
                drop()
                dfs(count+1)
                graph = og_graph
            

def block_break(s_r, s_c):
    global graph

    visited = [[0]*w for _ in range(h)]
    visited[s_r][s_c] = 1
    que = deque([(s_r,s_c,graph[s_r][s_c])])
    graph[s_r][s_c] = 0

    while que:
        x,y,area = que.popleft()
        for k in range(area):  # range(1, area)도 상관 x but 이게 더 빠름
            for dx,dy in move:
                nx,ny = x+dx*k,y+dy*k

                if 0<=nx<h and 0<=ny<w:
                    if visited[nx][ny] == 0 and graph[nx][ny] != 0:
                        visited[nx][ny] = 1
                        que.append((nx,ny,graph[nx][ny]))
                        graph[nx][ny] = 0
def drop():
    global graph

    temp = deque()
    for i in range(w):
        for j in range(h):

            if graph[j][i] == 0:
                up_j = j-1
                while graph[up_j][i] != 0 and up_j>=0:
                    temp.append(graph[up_j][i])
                    graph[up_j][i] = 0
                    up_j -= 1

                up_j2 = j
                while temp:
                    tmp = temp.popleft()
                    graph[up_j2][i] = tmp
                    up_j2 -= 1

t = int(input())
move = [(0,1),(0,-1),(1,0),(-1,0)]
for tc in range(t):
    n, w, h = map(int,input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]
    answer = 99999
    dfs(0)
    print(f'#{tc+1} {answer}')

# 벽돌 부수는 과정 -> bfs
# 벽돌 떨구는 과정 -> 구현
# 구슬 떨어뜨리는 과정 -> dfs