# N = int(input())

# d = [list(map(int, input().split())) for _ in range(N)]

# c = []

# for i in range(N):
#     for j in range(N):
#         c.append(d[i][j])

#         for a in range(1, N-1):
#             for b in range(1, N-1):

# 우하, 좌하, 좌상, 우상
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

T = int(input())

def dessert_run(r, c, turn1, turn2):
    dessert_set = set()

    # 0번 방향 수, 1번 방향 수, 2번 방향 수, 3번 방향 수
    counts = [turn1, turn2, turn1, turn2]

    for dir in range(4):
        for i in range(counts[dir]):
            r += dr[dir]
            c += dc[dir]

            if desserts[r][c] in dessert_set:
                return -1
            dessert_set.add(desserts[r][c])

    return len(dessert_set)

for tc in range(1, T+1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]
    answer = -1

    # 1. 시작점 정해주기
    for s_r in range(N-2):
        for s_c in range(1, N-1):

            # 2. turn1(우하), turn2(좌하)
            for turn1 in range(1, N-s_c):
                for turn2 in range(1, N-s_r-turn1):

                    if s_c-turn2 >= 0 and (turn1+turn2)*2 > answer: # 최댓값이 될 수 있는 경우만 확인 (가지치기)
                        answer = max(answer, dessert_run(s_r, s_c, turn1, turn2))

    print(f'#{tc} {answer}')






