# SWEA 2112. [모의 SW 역량테스트] 보호 필름

def test_films(films):
    for c in range(W):
        count = 0
        before = -1
        test_pass = False
        for r in range(D):
            if films[r][c] == before:
                count += 1
            else:
                count = 1
                before = films[r][c]
             
            if count >= K:
                test_pass = True
                break
        if not test_pass:
            return False
    return True

def dfs(films, count, idx):
    global answer

    # 1번 탈출 조건
    if test_films(films):
        answer = min(answer, count)

    # 지금까지 발견된 가장 작은 층수랑, 세본거
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
        # 다음 행 넘어가기 전에 의사 결정한 거 원복시켜
        next_films[i] = films[i]



T = int(input())

# 소괄호에 쉼표 써야 튜플 인식
A = (0,) * 20
B = (1,) * 20

# 참조점만 바꾸는 건 얕은복사

for tc in range(1, T+1):
    D, W, K = map(int,input().split())
    films = [list(map(int,input().split())) for _ in range(D)]

    answer = K

    # dfs에게 세가지 상태를 넘겨줄거임
    # 1. 현재 필름의 상태, 2. 지금까지 고른 층의 수, 3. 골라놓은 거 다음만 탐색할거라서 조합 -> idx
    # 부분집합으로 접근할거라서 dfs 채택
    # 부분집합은 두가지 방법 1. 넣을지 말지 2. 조합으로 짜도된다

    dfs(films, 0, 0)
    print(f'#{tc} {answer}')