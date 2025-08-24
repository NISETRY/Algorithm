T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    stat = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        for d in range(1, j+1):
            right = i+d-1
            left = i-d-1
            
            if left < 0 or right >= N:
                break

            if stat[left] == stat[right]:
<<<<<<< HEAD
                # 0 <-> 1
                stat[right] = 1 - stat[right]
                stat[left] = 1 - stat[left]
            else:
                break

=======
                # 0 <-> 1 을 바꿔야 함
                stat[right] = 1 - stat[right]
                stat[left] = 1 - stat[left]
            
>>>>>>> a29b2439cdd3ff779b66fe5c6a4f02e7936ecbc1
    print(f'#{tc+1}', *stat)