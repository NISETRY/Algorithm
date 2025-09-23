############### 강사님 코드 ################

# 완전탐색 => 이유 경우의 수를 고려; 총 3^13(바꾸는 경우의 수: X, A, B) * 20(W) * 13(D)
# DFS vs BFS => 최단 거리 문제와 유사 => BFS로 접근 => 벗!! 메모리가 넘어설 수도, 3^13 개의 arr을 저장해야 함
# 하지만 BFS로 풀 수 있음. 모든 배열을 저장하지 않는 방법 존재
def dfs(films, count, idx):
    global answer

    if test_films(films):
        answer = min(answer, count)

    if answer <= count:
        return

    if count == K-1:
        return

    next_films = films[:]
    for i in range(idx, D):
        next_films[i] = A
        dfs(next_films, count+1, i+1)
        next_films[i] = B
        dfs(next_films, count+1, i+1)


T = int(input())

A = (0,) * 20 # 미리 0으로 채워진 배열을 만들고 참조점만 바꾸는 식으로 접근
B = (0,) * 20

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]

    answer = K

    dfs(films, 0, idx)         # 조합을 변형하여 부분 집합을 구할 수 있고 이 부분 집합으로 구할 수 있음

