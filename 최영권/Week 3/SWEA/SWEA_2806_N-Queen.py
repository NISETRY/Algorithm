T = int(input())
for tc in range(1, T+1):
 
    N = int(input())
    pos = [0] * N
    flag_a = [False] * N
    flag_b = [False] * (2 * N - 1)
    flag_c = [False] * (2 * N - 1)
    def put():
        for j in range(N):
            for i in range(N):
                print('■' if pos[i] == j else '□', end=' ')
            print()
        print()
    count = 0
    def set(i):
        global count
        for j in range(N):
            if (not flag_a[j]
                and not flag_b[i + j]
                and not flag_c[i - j + (N - 1)]):
                pos[i] = j
                if i == (N - 1):
                    count += 1
                else:
                    flag_a[j] = flag_b[i + j] = flag_c[i - j + (N - 1)] = True
                    set(i + 1)
                    flag_a[j] = flag_b[i + j] = flag_c[i - j + (N - 1)] = False

    set(0)

    print(f"#{tc} {count}")