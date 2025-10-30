from copy import deepcopy
from pprint import pprint
from collections import deque
n,m,k = map(int, input().split()) # 사이즈, 나무 개수, 년도
graph = [[deque() for _ in range(n)] for _ in range(n)] # 나무 그래프
og_nutrition = [list(map(int, input().split())) for _ in range(n)] # 영양
now_nutrition = [[5]*n for _ in range(n)] # 누적 영양
move = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
dead = []

for _ in range(m):
    r,c,age = map(int, input().split())
    graph[r-1][c-1].append(age)

for _ in range(k):
    dead_trees = [[[] for _ in range(n)] for _ in range(n)]  # 봄에 죽은 나무 저장용

    # 봄
    for i in range(n):
        for j in range(n):
            if not graph[i][j]:
                continue

            alive = deque()
            for _ in range(len(graph[i][j])):
                age = graph[i][j].popleft()
                if now_nutrition[i][j] >= age:
                    now_nutrition[i][j] -= age
                    alive.append(age + 1)
                else:
                    dead_trees[i][j].append(age)
            graph[i][j] = alive


    # 여름
    
    for i in range(n):
        for j in range(n):
            if dead_trees[i][j]:
                for age in dead_trees[i][j]:
                    now_nutrition[i][j] += age // 2
    
    # 가을
    
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                
                for tree in range(len(graph[i][j])):
                    if graph[i][j][tree]%5 == 0:
                        for dx,dy in move:
                            if 0<=i+dx<n and 0<=j+dy<n:
                                graph[i+dx][j+dy].appendleft(1)
    
    # 겨울
    
    for i in range(n):
        for j in range(n):
            now_nutrition[i][j] += og_nutrition[i][j]


answer = 0
for i in range(n):
    for j in range(n):
        
        if graph[i][j]:
            for tree in range(len(graph[i][j])):
                answer += 1
print(answer)
