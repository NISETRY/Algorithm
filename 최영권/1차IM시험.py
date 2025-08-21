T = int(input())

for tc in range(1,T+1):
    N = int(input())
    position = 1
    rooms = list(range(1, N+1))
    moves = list(map(int, input().split()))

    visited = [1]
    count = 0
    while position < N:
        if position not in visited:
            visited.append(position)
            position = moves[position-1]
            count += 1
        else:
            position += 1
            count += 1


    print(f"#{tc} {count}")