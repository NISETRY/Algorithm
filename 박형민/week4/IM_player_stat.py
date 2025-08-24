T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())
    players = list(map(int, input().split()))

    ans = 0

    for i in range(N):
        for j in range(i + 1, N):
            if abs(players[i] - players[j]) <= K:
                ans += 1

    print(f'#{tc} {ans}')       # 실력 차가 K 이내인 팀원의 수를 구하시오


    N, K = map(int, input().split())
    stats = list(map(int, input().split()))

    ans = 1     # 1명인 팀은 기정 사실, 2명 이상 팀이 구성되는지만 확인하면 됨

    # sorted(stats) => 원본은 놔두고 새로운 값 return
    stats.sort()    # => 원본 값 바꿔버림; 원본을 변환해서 쓸 것이기 때문에 ㄱㅊ

    for i in range(N-1):
        temp = 1    # 초기값이 1인 이유: 팀원의 명수를 사용해야 하기 때문에 i번째에 있는 본인을 포함해야 함
        for j in range(i+1, N):
            if stats[j] - stats[i] > K:     # > K 인 이유는 break를 걸기 위해; 중간에 K가 넘으면 뒤도 어차피 안됨
                break
            
            temp += 1
        ans = max(ans, temp)

    print(f'#{tc} {ans}')

    ans = 1
    left = 0
    right = 0

    while right < N:
        if stats[right] - stats[left] <= K:
            right += 1
            ans = max(ans, right - left + 1)
            continue
        left += 1

    print(ans)