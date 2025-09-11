def check(film, D, W, K):
    for i in range(W):
        found = False
        for j in range(D-K+1):
            first_value = film[j][i]
            all_same = True

            for offset in range(1, K):
                if film[j+offset][i] != first_value:
                    all_same = False
                    break

            if all_same:
                found = True
                break

        if not found: # found == False
            return False
    return True


def dfs(depth, count):
    global answer, film

    # 가지치기: 현재 변경 횟수가 최소값 이상이면 볼 필요 없음
    if count >= answer:
        return
    
    if check(film, D, W, K):
        answer = min(answer, count)
        return
    
    # 모든 행을 다 바꿔봤으면 종료
    if depth == D:
        return
    
    original = film[depth][:]

    # 안 바꾸고 검사
    dfs(depth + 1, count)

    # 0인 줄 추가하기
    film[depth] = [0] * W
    dfs(depth + 1, count + 1)

    # 1인 줄 추가하기
    film[depth] = [1] * W
    dfs(depth + 1, count + 1)

    # 원래 행 복구
    film[depth] = original

T = int(input())

for tc in range(1, T+1):

    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    answer = K

    if check(film, D, W, K) == True:
        result = 0
    else:
        dfs(0, 0)
        result = answer

    print(f'#{tc} {result}')