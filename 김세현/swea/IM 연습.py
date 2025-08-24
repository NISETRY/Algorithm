# swea_22375_스위치 조작
T = int(input())

for tc in range(T):
    N = int(input())
    stat_in = list(map(int, input().split())) # 조작 전 스위치 상태
    stat_out = list(map(int, input().split())) # 조작 후 스위치 상태
    count = 0

    for i in range(N):
        if stat_in[i] != stat_out[i]:
            for i in range(N):
                stat_in[i] = 1 - stat_in[i]
                
            count += 1


    print(f'#{tc+1} {count}')
