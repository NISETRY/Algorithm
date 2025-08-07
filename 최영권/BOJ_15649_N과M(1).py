N, M = map(int, input().split())

numbers = [i for i in range(1, N+1)]
picked = []
visited = [0] * N

def permute(count):
    if count == M:
        for picknum in picked:
            print(picknum, end = ' ')
        print()
        return
    
    for idx in range(len(numbers)):
        if visited[idx] == 0:
            picked.append(numbers[idx])
            visited[idx] = 1
            permute(count + 1)
            picked.pop()
            visited[idx] = 0

permute(0)