N, M = map(int, input().split())
numbers = list(range(1, N+1))
# vistied 필요 없음
picked = []
# N과 M(2)
def comb(count, position):
    if count == M:
        for i in picked:
            print(i, end =' ')
        print()
        return

    for i in range(position, len(numbers)):
        picked.append(numbers[i])
        position += 1
        comb(count+1, position)
        position += 1
        picked.pop()
        position -= 1

        
comb(0, 0)

# N과 M(4)
def comb_repeat(count, position):
    if count == M:
        for i in picked:
            print(i, end =' ')
        print()
        return

    for i in range(position, len(numbers)):
        position -= 1
        picked.append(numbers[i])
        position += 1
        comb(count+1, position)
        picked.pop()
        position += 1

# comb_repeat(0, 0)