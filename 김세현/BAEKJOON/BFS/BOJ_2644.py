from collections import deque

n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input()) # 관계의 개수
arr = [[] for _ in range(n+1)] # 인접리스트 생성
visited = [False] * (n+1)
result = -1

for _ in range(m):
    x, y = map(int, input().split()) # 부모와 자식간의 관계
    arr[x].append(y)
    arr[y].append(x)

def dfs(current, cnt):
    global result
    visited[current] = True

    if current == b:
        result = cnt
        return

    for i in arr[current]:
        if visited[i] == False:
            dfs(i, cnt+1)
            if result != -1:
                return

dfs(a, 0)

print(result)



