T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input()))
    cnt = 0
    m_val = 0

    for i in lst:
        if i == 1:
            cnt += 1
            m_val = max(cnt, m_val)

        else:
            cnt = 0

    print(f'#{tc} {m_val}')