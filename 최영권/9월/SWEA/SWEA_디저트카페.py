import pprint
T = int(input())

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]
def dfs(row, col, start_r, start_c, dir, cnt, visited):
    global answer

    for d in range(dir, 4):  # 직진하거나 오른쪽으로만 꺾기
        nr, nc = row + dr[d], col + dc[d]

        # 격자 안에 있을 때만 진행
        if 0 <= nr < N and 0 <= nc < N:
            # 출발지로 돌아오는 경우 (사이클 완성)
            if nr == start_r and nc == start_c and cnt >= 4:
                answer = max(answer, cnt)
                return

            # 이미 먹은 디저트는 가지치기
            if course[nr][nc] in visited:
                continue
            
            visited.add(course[nr][nc])           # 방문 체크
            dfs(nr, nc, start_r, start_c, d, cnt+1, visited)
            visited.remove(course[nr][nc])        # 백트래킹



for tc in range(1, T+1):
    N = int(input())

    course = [list(map(int, input().split())) for _ in range(N)]
    answer = -1
    for r in range(N):
        for c in range(N):
            visited = set()
            visited.add(course[r][c])
            dfs(r, c, r, c, 0, 1, visited)  # 시작점, 방향0, 카운트1
    print(f"#{tc} {answer}")
