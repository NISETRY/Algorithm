T = int(input())
for tc in range(1, T+1):
    N = int(input())

    Fst = list(map(int, input().split())) # status of First
    Lst = list(map(int, input().split())) # status of Last

    Dur = Fst  # status During process
    cnt = 0

    for i in range(N):
        if Fst[i] != Lst[i]:
            for j in range(i, N):
                Dur[j] = 1 - Dur[j]
            cnt += 1

    print(f'#{tc} {cnt}')