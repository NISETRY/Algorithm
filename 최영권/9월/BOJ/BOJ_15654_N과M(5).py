N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
picked = []
visited = [0] * N 
def comb(cnt, idx):
    if cnt == M:
        print(*picked)
        return
    for i in range(idx, N):
            picked.append(numbers[i])
            comb(cnt+1, i)
            picked.pop()


comb(0, 0)