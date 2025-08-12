for tc in range(10):

    N = 8
    num = int(input())

    arr = [list(input().strip()) for _ in range(N)]

    count = 0

    # 가로 방향 회문 찾기
    for i in range(N):
        for j in range(N - num + 1): 
            word = arr[i][j:j+num]
            if word == word[::-1]:
                count += 1

    # 세로 방향 회문 찾기
    for i in range(N - num + 1):
        for j in range(N):
            word = ""
            for k in range(num):
                word += arr[i+k][j]
            if word == word[::-1]:
                count += 1

    print(f'#{tc+1} {count}')