T = int(input())

for tc in range(T):

    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))

    pos = 0 # 현재 위치를 나타냄
    count = 0 # 충천 횟수

    # pos 부터 pos + k 사이에 충전소 갯수를 확인하면? 
    # 만약 1개면 바로 충전, 2개면 나중 충전소에서 충전

    while pos + K < N:
        for step in range(K, 0, -1):
            if (pos+step) in charge:
                pos += step
                count += 1
                break

        else:
            count = 0
            break

    print(f'#{tc+1} {count}')